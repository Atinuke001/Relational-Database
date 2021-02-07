select * from
        (select Year(InvoiceDate) as Year,datename(MONTH,InvoiceDate) as month, SUM(il.Quantity * il.UnitPrice) as total_sales from Sales.InvoiceLines as il ,Sales.Invoices as si where il.InvoiceID = si.InvoiceID
		group by Year(InvoiceDate),  datename(MONTH,InvoiceDate)) as monthly_sales
		Pivot(SUM(total_sales) for month in ([January],[February],[March],[April],[May],[June],[July],[August],[September],[October],[November],[December])) AS MNamePivot
		order by Year



