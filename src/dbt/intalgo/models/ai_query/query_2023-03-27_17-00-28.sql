

--

select count(*), main.ORGS.Name
  from main.ORGS
  join main.PEEPS 
    on main.ORGS."Organisation ID" = main.PEEPS."Organisation ID"
group by main.ORGS.Name