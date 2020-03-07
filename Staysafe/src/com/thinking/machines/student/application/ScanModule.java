package com.thinking.machines.school.application;
import java.io.*;
import java.net.*;
public class ScanModule
{
ScanModule()
{
try
{
Process p = Runtime.getRuntime().exec("python scan.py ");
BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
String ret = new String(in.readLine()).toString();
System.out.println(ret);
int c1=ret.indexOf("'");
int c2=ret.indexOf("'",c1+1);
int c3=ret.indexOf(" ");

String pc1=ret.substring(c1+1,c3);
String pc2=ret.substring(c3+1,c2);


 


System.out.println("value is : "+pc1+","+pc2);
}catch(Exception e){}
}
}
