SELECT 
  ORGS.Name as Organisation,
  COUNT(PEEPS.Index) AS PeopleCount
FROM 
  {{ source('intalgo', 'ORGS') }} ORGS
INNER JOIN 
  {{ source('intalgo', 'PEEPS') }} PEEPS
ON 
  ORGS.Index = PEEPS.ORGS_INDEX
GROUP BY
  ORGS.Name;