% clear all
% close all
% clc

t1 = datetime(2020,2,5);

for i=0:109
a(i+1) = t1+caldays(i);
disp(a(i+1))
end

% a=flipud(a);
% load A
% 
 d=table2array(A(2:end,4));
 d=char(d);
 a=d(1:end,[1:10 12:25]);
 temp=datenum(datetime(a,'InputFormat',['yyyy-MM-ddHH:mm:ss-HH:mm']));
 temp=sort(temp);
% 
% 1
 [n v]= hist(temp);
 v=datestr(v,'dd-mm-yyyy')
 
 disp

