def main():
    item=[]
    restockItem=[]
    restockQuantity=[]
    problemRow=0
    totalRevenue=0
    RESTOCK_THRESHOLD = 5
    try:
        with open ("sales_log.txt", "r") as f:
            next(f)
            lines = f.readlines()
            totalRow = len(lines)
            for i,line in enumerate(lines):
                line=line.strip()
                if line.startswith('#') or not line:
                    problemRow+=1
                    continue
                data = line.strip().split(",")
                if len(data) < 3:
                    problemRow+=1
                    continue
                elif len(data) > 3:
                    data = data[:3]
                try:
                    fprice = float(data[1])
                    iquantity = int(data[2])
                except ValueError:
                    problemRow+=1
                    continue
                if iquantity < RESTOCK_THRESHOLD:
                    restockQuantity.append(RESTOCK_THRESHOLD-iquantity)
                    restockItem.append(data[0])
                item.append(data)
                revenue = float(data[1])*int(data[2])
                totalRevenue += revenue
            print(f"{'Restock Item':^15}{'Quantity'}")
            restock = list(zip(restockItem,restockQuantity))
            for i,(item,quantity) in enumerate(restock,1):
                print(f"{i}:{item:<15}{quantity}")
            print("-"*50)
            print(f"Total Revenue is RM{totalRevenue:.2f}")
            print("-"*50)
            print(f"Total Rows  : {totalRow}")
            print(f"Problem Rows: {problemRow}")
            print(f"{(problemRow/totalRow)*100:.2f}% of Problem Row")
            write(restock,totalRevenue)


    except FileNotFoundError:
        print("File not found")


def write(data,totalRevenue):
    with open("business_report.txt", "w") as f:
        f.write("Total Revenue = " + "RM" + str(totalRevenue) + "\n")
        f.write("Restock Item List\n")
        for i, (item, quantity) in enumerate(data, 1):
            f.write(f"{i}: {item}, Need: {quantity}\n")


main()