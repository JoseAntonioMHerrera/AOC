#include <glib.h>

#ifndef _MASKED_DATA_H
#define _MASKED_DATA_H

#define INIT_CAPACITY_DIR_AND_VALUES 10
#define INIT_CAPACITY_MD_VECTOR 10

#define MASKED_DATA_INIT(masked_data) masked_data_init(&masked_data)
#define ADD_DIRECTION_AND_VALUE(masked_data, value, memory) add_direction_and_value(masked_data, value, memory)
#define ADD_MASK(masked_data,mask) add_mask(masked_data,mask)
#define GET_MEMORY_AND_VALUE(masked_data, index) get_memory_and_value(&masked_data, (const int) index)
#define GET_MEMORY_AND_VALUE_SIZE(masked_data) get_memory_and_value_size(&masked_data);
#define APPLY_MASK_TO_INDEX(masked_data, index) apply_mask_to_index(&masked_data, (const int) index)
#define APPLY_MASK_TO_MEMORY_ADDRESS(masked_data,output) apply_mask_to_memory_address(&masked_data, output)
#define ADD_MASKED_DATA(md_vector,masked_data) add_masked_data(md_vector,masked_data)
#define MD_VECTOR_INIT(md_vector) md_vector_init(md_vector)
#define GET_LAST_MASKED_DATA(md_vector) get_last_masked_data(md_vector)

typedef struct MemoryAndValue {
    unsigned long long* value;
    unsigned* memory; 
} MemoryAndValue;

typedef struct MaskedData{
    char* mask;
    GArray* directions_and_values;
} MaskedData;

typedef struct MDVector{
    MaskedData* md_vector;
    int size;
    int total;
} MDVector;

void masked_data_init(MaskedData**);
void add_mask(MaskedData*,char*mask);
void add_direction_and_value(MaskedData*, unsigned long long*, unsigned*);
MemoryAndValue* get_memory_and_value(MaskedData*, const int);
int get_memory_and_value_size(MaskedData*);
void apply_mask_to_index(MaskedData*,const int);
static void vector_resize(MDVector**,int);
void add_masked_data(MDVector**,MaskedData*);
void md_vector_init(MDVector**);
MaskedData* get_last_masked_data(MDVector*);

#endif