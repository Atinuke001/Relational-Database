CREATE TRIGGER trig_Update_Employee
ON [tb_EmergencyContact]
FOR INSERT
AS
Begin
    Insert into tb_EmergencyContact_V (empid,firstname,lastname) 
    Select Distinct i.empid, i.firstname,i.lastname 
    from Inserted i
    Left Join tb_EmergencyContact_V e
    on i.empid = e.empid and i.firstname = e.firstname and i.lastname = e.lastname 
    where e.empid is null
End


select * from tb_EmergencyContact_V