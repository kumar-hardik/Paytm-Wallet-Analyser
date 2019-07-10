#import panda for dataframe manipulation 
import pandas as pd
#import matplotlib for visualization
import matplotlib.pyplot as plt


#read the CSV file
df=pd.read_csv("/home/FRACTAL/hardik.kumar/Desktop/mypaytm.csv")
"""
IMPORTANT some users may get an error with csv file. Then convert the CSV file into an excel file and run the following command:

df= pd.read_excel("/home/FRACTAL/hardik.kumar/Desktop/mypaytm.xlsx")
"""

#fill all the nan value to zero
df.fillna({'Debit':0,'Credit':0},inplace=True)

#fetach all the cashback.
#Note:check in your csv file, in some CSV it is Bonus Added instead of Cashback Received
df_check_cashback=df[['Date','Credit']][df['Activity']=='Cashback Received']

#convert date coloumn to date time value. It will help in sorting , sum and group by operation
df_check_cashback['Date']=pd.to_datetime(df_check_cashback['Date'])

#add all the cashback according to month
df_cashback=df_check_cashback.groupby(df_check_cashback['Date'].dt.strftime('%B'))['Credit'].sum()

#save the cashback file in ypur desired local destination.
df_cashback.to_csv("/home/FRACTAL/hardik.kumar/Desktop/paytmcashback.csv")


#convert main dataframe date coloumn to date time value. It will help in sorting , sum and group by operation
df['Date']=pd.to_datetime(df['Date'])

#group the debit and credit of month 
summary_by_month=df.groupby(df['Date'].dt.strftime('%B'))['Debit','Credit'].sum()

#save the file.check path accoring to your desired local destination.
summary_by_month.to_csv("/home/FRACTAL/hardik.kumar/Desktop/paytm_summary.csv")

#read the summary file
df_paytm_summary=pd.read_csv("/home/FRACTAL/hardik.kumar/Desktop/paytm_summary.csv")

#read tthe cashback file
df_cashback=pd.read_csv("/home/FRACTAL/hardik.kumar/Desktop/paytmcashback.csv",header=None,names=["Month","Cashback"])


print("***Welcome to the magic of python***")
#prinf the summary file
print("\nYour's paytm summary\n\n",df_paytm_summary)

#print the cashback file
print("\nYour's total cashback\n\n",df_cashback)


print("\nFull summary\n")
#print total debit in a year for my case according to csv file
print("\nTotal Debit ",df['Debit'].sum()," Rs.")
#print total credit in a year for my case according to csv file
print("\nTotal Credit" ,df['Credit'].sum()," Rs.")
#print total cashback in a year for my case according to csv file
print("\nTotal Cashback",df_cashback['Cashback'].sum()," Rs.")
#print total cashabck percentage against debit in a year for my case according to csv file
print("\nTotal Cashback Percentage",df_cashback['Cashback'].sum()/(df['Debit'].sum())*100," %")

print("\nNow plot figure to visualize data\n")

#create the plot
plt.figure(figsize=(20,20))

#take all 12 month debit values
y1=df_paytm_summary['Debit']

#take all 12 month credit values
y2=df_paytm_summary['Credit']

#take all 12 month on x axis
x=df_paytm_summary['Date']
xc=df_cashback['Month']

#take all 12 month cashback values
yc=df_cashback['Cashback']


plt.title('Paytm')
plt.xlabel("Date") # X-Axis 
plt.ylabel("Debit/Credit") # Y-Axis

#plot the chart of the credit/debit against month
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(xc,yc)

#check top right corner on graph and will indicate color of the line
plt.legend(['Debit','Credit','Cashback','mean'],loc=1)
plt.savefig('/home/FRACTAL/hardik.kumar/Desktop/paytmfig.pdf', format='pdf')
