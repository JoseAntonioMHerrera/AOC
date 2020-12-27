#include "maskedvalues.h"
#include <glib.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

static void vector_resize(MDVector** mv ,int new_size){
    (*mv)->md_vector = realloc((*mv)->md_vector,sizeof(MaskedData)*new_size);
    (*mv)->total = new_size;
}

void masked_data_init(MaskedData** m_data){
    *m_data = malloc(sizeof(MaskedData));
    (*m_data)->directions_and_values = g_array_new(0,0, sizeof(MemoryAndValue*));
}

void add_mask(MaskedData* md, char* mask){
    md->mask = mask;
}

void add_direction_and_value(MaskedData* m_data, unsigned long long* value, unsigned* memory){
    if(m_data == NULL || m_data == 0){
        masked_data_init(&m_data);
    }
    MemoryAndValue* m_a_v = (MemoryAndValue*) malloc(sizeof(MemoryAndValue));
    m_a_v->memory = memory;
    m_a_v->value = value;
    g_array_append_val(m_data->directions_and_values,m_a_v); 
}

MemoryAndValue* get_memory_and_value(MaskedData* m_data, const int index){
    return g_array_index(m_data->directions_and_values,MemoryAndValue*,index);
}
void apply_mask_to_index(MaskedData* m_data,const int index){
    if(index < m_data->directions_and_values->len){
        int mask_size = strlen(m_data->mask)-1;
        int j;
        unsigned long long pow_value = 0;
        MemoryAndValue* m_a_v = g_array_index(m_data->directions_and_values,MemoryAndValue*,index);
        for(j=0; j <= mask_size; j++){
            pow_value = (unsigned long long) pow(2,j);
            if(m_data->mask[mask_size - j] == '1'){
                *m_a_v->value = *m_a_v->value | pow_value;
            }else if(m_data->mask[mask_size - j] == '0'){
                *m_a_v->value = *m_a_v->value & (~pow_value);
            
            }
        }
    }
}


void md_vector_init(MDVector** md_v){
    (*md_v) = malloc(sizeof(MDVector));
    (*md_v)->md_vector = (MaskedData*) malloc(sizeof(MaskedData)*INIT_CAPACITY_MD_VECTOR);
    (*md_v)->size = 0;
    (*md_v)->total = INIT_CAPACITY_MD_VECTOR;
}

void add_masked_data(MDVector** md_v, MaskedData* masked_data){
    if(*md_v == 0 || *md_v == NULL){
        md_vector_init(md_v);
    }else if((*md_v)->size >= (*md_v)->total){
        vector_resize(md_v,(*md_v)->size*2);
    }
    (*md_v)->md_vector[(*md_v)->size] = *masked_data;
    (*md_v)->size+=1;
}

MaskedData* get_last_masked_data(MDVector* md){
    return &md->md_vector[md->size - 1];
}