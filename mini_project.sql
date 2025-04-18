

select top 20*
from [sale].[supermarket_sales]


-- tổng số đơn hàng được order
select 
    count(sms.[Invoice_ID]) as [Total Order]
from [sale].[supermarket_sales] as sms

-- tổng doanh số theo từng Branch. Kết quả làm tròn đến 2 chữ số thập phân 

select 
    sms.[Branch],
    round(sum(sms.[Unit_price]*sms.[Quantity]),2) as [Sum Sale]
from [sale].[supermarket_sales] as sms
group by sms.[Branch]


-- tổng doanh số và số lượng đơn hàng của từng ProductLine
select 
    sms.[Product_line],
    round(sum(sms.[Unit_price]*sms.[Quantity]),2) as [Sum Sale],
    count(sms.[Invoice_ID]) as [Total Order]
from [sale].[supermarket_sales] as sms
group by sms.[Product_line]

-- tổng doanh số, tổng số đơn hàng của từng loại khách hàng theo từng Productline.(tổng doanh số làm tròn đến 2 chữ số thập phân)
go
create view [Product for Cus] as
select 
    sms.[Product_line],
    sms.[Customer_type],
    round(sum(sms.[Unit_price]*sms.[Quantity]),2) as [Sum Sale],
    count(sms.[Invoice_ID]) as [Total Order]
from [sale].[supermarket_sales] as sms
group by sms.[Product_line],sms.[Customer_type]
go 

select * from [Product for Cus]

-- các khung giờ có tổng số đơn hàng cao hơn số lượng đơn hàng trung bình theo giờ của tháng
go 
create view [Max Sale Month] as --Tao view tinh tong doanh thu va tong don hang theo tung thang
select 
    datepart(year, [Date]) as [Year],
    datepart(month, [Date]) as [Month],
    round(sum([cogs]), 2) as [Sum Sale],
    count([Invoice_ID]) as [Total Order]
from [sale].[supermarket_sales]
group by datepart(month, [Date]), datepart(year, [Date])
go 

go
create view [Order for each Hour] as --Tao view tinh tong don hang theo gio cua thang co doanh so cao nhat
select 
    datepart(month, [Date]) as [Month],
    datepart(hour, [Time]) as [Hour of month],
    count([Invoice_ID]) as [Total Order]
from [sale].[supermarket_sales]
where datepart(month, [Date]) = (select m.[Month]
                                    from(select top 1* from [Max Sale Month] as mm order by mm.[Sum Sale] desc) as m)
group by datepart(hour, [Time]),datepart(month, [Date])
go

go 
create view [Avg for order] as --Tao view tinh so don hang trung binh theo gio cua thang co doanh so cao nhat
select 
    m.[Month],
    nh.[Number hour] as [Number hour],
    (m.[Total Order]/nh.[Number hour]) as [Avg Order]
from (select top 1* from [Max Sale Month] as mm order by mm.[Sum Sale] desc) as m
join (select count(oeh.[Hour of month]) as [Number hour], oeh.[Month] 
            from [Order for each Hour] as oeh group by oeh.[Month]) as nh
on m.[Month] = nh.[Month]
group by m.[Month], nh.[Number hour], m.[Total Order]
go

--Dua ra cac khung gio co luong don hang cao hon trung binh cua thang
select 
    oeh.[Hour of month],
    oeh.[Total Order]
from [Order for each Hour] as oeh
join [Avg for order] as aod 
on oeh.[Month] = aod.[Month]
where oeh.[Total Order] > aod.[Avg Order]


-- Với mỗi Product line, đều có 2 loại khách hàng (Customer Type) mua hàng là Normal, Member. 
select pfc.*
from [Product for Cus] as pfc 
join (select
            pfc.Product_line,
            min([Total Order]) as [Total Order],
            max([Sum Sale]) as [Sum Sale]
        from [Product for Cus] as pfc 
        group by pfc.Product_line) as pl 
on pfc.Product_line = pl.Product_line
where pl.[Total Order] = pfc.[Total Order]
    and pl.[Sum Sale] = pfc.[Sum Sale]


-- tổng doanh số, tổng số đơn hàng theo tháng, tổng doanh số và tổng số đơn hàng của các tháng về trước
-- lay cot before month
select 
    *,
    sum(mm.[Sum Sale])over(order by mm.[Month] ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING) as [Sum sale Before],
    sum(mm.[Total Order])over(order by mm.[Month] ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING) as [Total order Before]
from [Max Sale Month] as mm


