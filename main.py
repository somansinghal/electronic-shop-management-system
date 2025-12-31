import pandas as pd
while True:
    print("Welcome to Electronics Shop Management System.")
    print("1.Add Product\n2.Show All Product\n3.Find Product\n4.Sales Of Day\n5.Bills Creating\n6.Delete Sold Product")
    print("7.Show All Bills\n8.Find Bill\n9.Graph of Product Name and Price\n10.Graph of Customer Name and Total Bill Amount\n11.Exit")
    ch=int(input("Enter choice : "))
    if ch==1:
      try:
          df=pd.read_csv('electronicssales_data.csv')
      except FileNotFoundError:
          df=pd.DataFrame(columns=['product-code','productname','price','quantity'])
      if df.empty:          max_productcode=100
      else:
          max_productcode=df['product-code'].max()
          next_productcode=max_productcode +1
      productname=input("Enter product name : ")
      price=float(input("Enter  product price : "))
      quantity=int(input("Enter quantity : "))
      new_data={'productcode':next_productcode,'productname':productname,
                'price':price,'quantity':quantity}
      df.loc[len(df.index)]=[next_productcode,productname,price,quantity]
      df.to_csv('electronicssales_data.csv',index=False)
    elif ch==2:
        try:
            df=pd.read_csv('electronicssales_data.csv')
            print(df)
        except FileNotFoundError:
            print("The CSV file 'electronicssales_data.csv' does not exist or is empty.")
    elif ch==3:
        try:
            df=pd.read_csv('electronicssales_data.csv')
            product_name_to_find=input("Enter the product name to search for :")
            result=df[df['productname']==product_name_to_find]
            if not result.empty:
                print("Found data for the product name :",product_name_to_find)
                print(result)
            else:
                print("No data found for the product name :",product_name_to_find)
        except FileNotFoundError:
            print("The CSV file 'electronicssales_data.csv' does not exist or is empty.")
    elif ch==4:
        try:
            df=pd.read_csv('electronicssales_data.csv')
        except FileNotFoundError:
            print("The CSV file 'electronicssales_data.csv' does not exist or is empty.")
            exit()
        product_name=input("Enter the product name : ")
        sales_quantity=int(input("Enter the sales quantity  : "))
        product_row=df[df['productname']==product_name]
        if not product_row.empty:
            product_index=product_row.index[0]
            product_price=product_row['price'].values[0]
            bill_amount=product_price * sales_quantity
            df.at[product_index,'quantity']-=sales_quantity
            df.to_csv('electronicssales_data.csv',index=False)
            print("Bill Amount : ",bill_amount)
            print("Updated CSV File with reduced quantity.")
        else:
            print(f"No product found with the name: {product_name}")
    elif ch==5:
        try:
            df=pd.read_csv('electronicssales_data.csv')
        except FileNotFoundError:
            print("The CSV file 'electronicssales_data.csv' does not exist or is empty.")
            exit()
        cust_name=input("Enter the customer name :")
        product_name=input("Enter the product name :")
        sales_quantity=int(input("Enter the sales quantity :"))
        product_row=df[df['productname']==product_name]
        if not product_row.empty:
            product_index=product_row.index[0]
            product_price=product_row['price'].values[0]
            bill_amount=product_price * sales_quantity
            df.at[product_index,'quantity']-= sales_quantity
            df.to_csv('electronicssales_data.csv',index=False)
            print("Bill Amount :",bill_amount)
            print("Updated CSV file with reduced quantity.")
            try:
                df=pd.read_csv('transcation.csv')
            except FileNotFoundError:
                df=pd.DataFrame(columns=['bill_no','cust_name','productname','price',
                                         'quantity','bill_amount','tran_type'])
            if df.empty:
                bill_no=1
            else:
                bill_no=df['bill_no'].max()
                bill_no=bill_no + 1
            t_type=input("Enter the transcation type : ")    
            result={'bill_no':bill_no,'cust_name':cust_name,'productname':product_name,
                      'price':product_price,'quantity':sales_quantity,'bill':bill_amount,
                      'tran_type':t_type}
            result=df.to_csv('transcation.csv',index=False)
            df.loc[len(df.index)]=[bill_no,cust_name,product_name,product_price,sales_quantity,bill_amount,t_type]
            df.to_csv('transcation.csv', index=False)
            print("successfully created")
        else:
            print(f"No product found with the name:{product_name}")
    elif ch==6:
        try:
            df=pd.read_csv('electronicssales_data.csv')
        except FileNotFoundError:
            print("The CSV file 'electronicssales_data.csv' does not exist or is empty")
            exit()
        product_name_to_delete=input("Enter the product name to delete : ")
        df=df[df['productname']!=product_name_to_delete]
        df.to_csv('electronicssales_data.csv', index=False)
        print(f"Record with product name '{product_name_to_delete}' have been deleted.")
    elif ch==7:
        try:
          df=pd.read_csv('transcation.csv')
          print(df)
        except FileNotFoundError:
           print("The CSV file 'transcation.csv' does not exist or is empty.")
    elif ch==8:
        try:
            df=pd.read_csv('transcation.csv')
            customer_name_to_find=input("Enter the customer name to search for : ")
            result=df[df['cust_name']==customer_name_to_find]
            if not result.empty:
                print("Found data for the customer name : ",customer_name_to_find)
                print(result)
            else:
                print("No data found for the customer name :",customer_name_to_find)
        except FileNotFoundError:
            print("The CSV file 'transcation.csv' does not exist or is empty")       
    elif ch==9:
        import matplotlib.pyplot as plt
        df.to_csv('electronicssales_data.csv')
        df=pd.read_csv('electronicssales_data.csv')
        x=df['productname']
        y=df['price']
        plt.bar(x,y)
        plt.xlabel('Product Name')
        plt.ylabel('Price of Product')
        plt.title('Product and Price Information')
        plt.show()
    elif ch==10:
        import matplotlib.pyplot as plt
        df.to_csv('transcation.csv')
        df=pd.read_csv('transcation.csv')
        x=df['cust_name']
        y=df['bill']
        plt.bar(x,y)
        plt.xlabel('Customer Name')
        plt.ylabel('Total Bill Amount')
        plt.title('Customer Name and Total Bill Amount')
        plt.show()
    elif ch==11:
        exit()
