select aa.* into dbo.access 
from (select * from dbo.Audit_Trail_201710_201801 union all 
      select * from dbo.Audit_Trail_201802_201805 union all 
	  select * from dbo.Audit_Trail_201806_201809) aa

--select distinct Card_Number, SUBSTRING(Location, 9, 7) as Gate_name, RIGHT(Location, 13) as pass  from dbo.access
select Date_Occurred, count(distinct Card_Number) as number into #tmp 
from dbo.access
where SUBSTRING(Location, 9, 7) in ('A01.08P','A01.09P','A01.10P','A01.11P','A01.12P','A01.13P') and
	  PATINDEX('%1%', RIGHT(Location, 13))>0
group by Date_Occurred
having Date_Occurred in (select Date_Occurred from dbo.[summation_no_weekend_holiday_error])
order by Date_Occurred

--select * from #tmp
--drop table #tmp

ALTER TABLE dbo.summation_no_weekend_holiday_error
ADD number int

update a set a.number=b.number 
from dbo.summation_no_weekend_holiday_error a,#tmp b 
where a.Date_Occurred=b.Date_Occurred
--5ÔÂ31ÈÕnull

select a.*, b.highest_temperature, b.lowest_temperature,b.weather_type, b.wind_direction, b.wind_scale
from dbo.summation_no_weekend_holiday_error a,dbo.weather_CN2EN b
where a.Date_Occurred = b.Date_Occurred