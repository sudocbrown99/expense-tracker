from storage import (
    initialize_expenses_storage,
)
from prompts import (
    prompt_start,
)

def main():
    initialize_expenses_storage()
    prompt_start()
main()

