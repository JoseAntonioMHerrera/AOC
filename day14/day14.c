#include <stdio.h>
#include <glib.h>
#include <regex.h>
#include <stdlib.h>
#include <errno.h>
#include "maskedvalues.h"
int errno;

void readFromFile(FILE* ftpr, MDVector** input){
    regex_t regex_mask;
    regex_t regex_mem_values;
    regmatch_t mask[2];
    regmatch_t mem_value[3];
    ssize_t read;
    size_t line_len = 10;
    char* line = (char*) malloc(line_len);
    char* mask_element;
    unsigned* memory_value = 0;
    unsigned long long* number_value = 0;
    char* str_regex_mask = "^mask = ([10X]*)*\0$";
    char* str_regex_memval = "^mem\\[([0-9]*)\\] = ([0-9]*)*\0$";
    char* line_mem_copy = 0;
    char* line_value_copy = 0;
    MaskedData* md = 0;

    MD_VECTOR_INIT(input);
    if(regcomp(&regex_mask,str_regex_mask,REG_EXTENDED)){
        fprintf(stderr, "Could not compile regex %s \n", str_regex_mask);
        exit(1);
    }
    
    if(regcomp(&regex_mem_values, str_regex_memval,REG_EXTENDED)){
        fprintf(stderr, "Could not compile regex %s \n", str_regex_memval);
        exit(1);
    }

    while((read = getline(&line,&line_len, ftpr)) > 0){
        if((regexec(&regex_mask,line,2,mask,REG_NOTEOL)) != 0){
            if((regexec(&regex_mem_values,line,3,mem_value,REG_NOTEOL)) == 0){
                line[mem_value[1].rm_eo] = '\0';
                line[mem_value[2].rm_eo] = '\0';
                memory_value = (unsigned*) malloc(sizeof(int));
                number_value = (unsigned long long*) malloc(sizeof(int));
                *memory_value = atoi(&line[mem_value[1].rm_so]);
                *number_value = atoi(&line[mem_value[2].rm_so]);
                md = GET_LAST_MASKED_DATA(*input);
                ADD_DIRECTION_AND_VALUE(md,number_value,memory_value);
            }
        }else{
            line[mask[1].rm_eo] = '\0';
            mask_element = (char*) malloc(mask[1].rm_eo - mask[1].rm_so);
            strcpy(mask_element, &line[mask[1].rm_so]);
            MASKED_DATA_INIT(md);
            ADD_MASK(md,mask_element);
            ADD_MASKED_DATA(input,md);
        }
    }

    regfree(&regex_mask);
    regfree(&regex_mem_values);
    free(line);
}

void buildMemoryTable(MDVector* m_data,GHashTable** cells){

    int i,j;
    (*cells) = g_hash_table_new(g_int_hash, g_int_equal);
    MemoryAndValue* m_and_v = 0;

    for(i = 0; i < m_data->size; i++){
        for(j = 0; j < m_data->md_vector[i].directions_and_values->len; j++){
            APPLY_MASK_TO_INDEX(m_data->md_vector[i],j);
            m_and_v = GET_MEMORY_AND_VALUE(m_data->md_vector[i],j);
            g_hash_table_insert(*cells,m_and_v->memory,m_and_v->value);
        }
    }
}

int main(){

    FILE* fptr;
    int errnum;
    fptr = fopen("input.txt","r");
    MDVector* input;
    GHashTable* mem_cells;
    unsigned long long sum = 0;
    if(fptr == NULL){
        errnum = errno;
        fprintf(stderr, "%s\n", strerror(errnum));
    }else{
        readFromFile(fptr,&input);
        fclose(fptr);
        
        buildMemoryTable(input,&mem_cells);
        GList* values = g_hash_table_get_values(mem_cells);
        GList* i;
        int count = 0;
        for(i = values; i != NULL; i = i->next){
            sum = sum + (*(unsigned long long*)i->data);
        }    
        printf("Resultado: %llu\n",sum);
    }
}