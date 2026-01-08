from storage import (
    initialize_expenses_storage, 
    read_expenses_storage, 
    write_expenses_storage, 
    storage_file, 
    gen_id, 
    modify_expenses_storage
)
from prompts import (
    prompt_start,
)

def main():
    initialize_expenses_storage()
    prompt_start()
main()

