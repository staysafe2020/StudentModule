package com.thinking.machines.school.dao;
import com.thinking.machines.school.dao.DAOException;
import java.sql.*;


public class DAOConnection 
{
private DAOConnection()
{
}
public static Connection getConnection() throws DAOException
{
try
{
Connection c;
Class.forName("org.apache.derby.ClientDriver");
c=DriverManager.getConnection("jdbc:derby://localhost:1527/schooldb");
return c;
}catch(Exception e)
{
throw new DAOException(e.getMessage());
}
}
}
