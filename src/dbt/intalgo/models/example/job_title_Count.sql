
-- Use the `ref` function to select from other models

select 'Job Title', COUNT(Index) 
from {{ source('intalgo', 'PEEPS') }}

