-- use MX_practices 

-- select * 
-- from [dbo].[SaleOrders]

-- select * from [dbo].[RankRFM]

-- Tính RFM_Score nhưng không chia từ 1 đến 5 mà chỉ từ 1 đến 4. 
-- R là bao lâu rồi chưa mua hàng
-- F là (số đơn/ số ngày mua hàng). Với số ngày mua hàng là từ min(orderdate) đến max(orderdate)
-- M là doanh thu từ khách hàng đấy

-- Gia dinh ngay tinh toan la 2017-07-01
go
with tb1 as (
    select 
        CustomerKey,
        datediff(day, max(OrderDate), '2017-07-01') as R,
        case 
            when datediff(day, min(OrderDate), max(OrderDate)) <> 0 then datediff(day, min(OrderDate), max(OrderDate))
            else 1
        end as 'Num_day',
        count(distinct OrderNumber) as 'NumOrder',
        sum(SalesAmount) as M
    from [dbo].[SaleOrders]
    group by CustomerKey
    ),
    tb2 as (
    select 
        CustomerKey,
        R,
        NumOrder/cast(Num_day as float) as F,
        M,
        percent_rank() over (order by R desc) as 'R_percent',
        percent_rank() over (order by NumOrder/cast(Num_day as float)) as 'F_percent',
        percent_rank() over (order by M) as 'M_percent'
    from tb1
    ),
    tb3 as (
    select 
        CustomerKey,
        case 
            when R_percent < 0.25 then '1'
            when R_percent < 0.5 then '2'
            when R_percent < 0.75 then '3'
            when R_percent <= 1 then '4'
        end as 'R_score',
        case 
            when F_percent < 0.25 then '1'
            when F_percent < 0.5 then '2'
            when F_percent < 0.75 then '3'
            when F_percent <= 1 then '4'
        end as 'F_score',
        case 
            when M_percent < 0.25 then '1'
            when M_percent < 0.5 then '2'
            when M_percent < 0.75 then '3'
            when M_percent <= 1 then '4'
        end as 'M_score'
    from tb2
    ),
    tb4 as (
    select
        Segment,
        trim([value]) as "Scores"
    from [dbo].[RankRFM]
    cross apply string_split(Scores, ',')
    )


select 
    CustomerKey,
    R_score, F_score, M_score,
    concat(R_score, F_score, M_score) as 'RFM_score',
    Segment
from tb3 
left join tb4
    on concat(tb3.R_score, tb3.F_score, tb3.M_score) = Scores


 

