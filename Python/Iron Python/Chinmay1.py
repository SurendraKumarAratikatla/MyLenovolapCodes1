tableInfo=SqlHelper.GetTable("Product_Item_Link_QuoteData")
MainItemCont=Product.GetContainerByName("Product_MainItem")
LineItemCont=Product.GetContainerByName("Product_LineItem")

Data = "select * from PRODUCT_ITEM_LINK_QUOTEDATA where UserID = '{}' and CartId = '{}'".format(Quote.UserId , Quote.QuoteId)
QuoteData = SqlHelper.GetList(Data)

for row in hell:
   tableInfo.AddRow({"CpqTableEntryId" : row.CpqTableEntryId})

SqlHelper.Delete(tableInfo)

tableInfo.NewBatch()
dataDict = dict()
for row in MainItemCont.Rows:
   dataDict[row["MainItem"]] = [row["Main_ItemName"]]

for item in LineItemCont.Rows:
   if item.IsSelected:
       tableInfo.AddRow({"UserId":Quote.UserId,
                         "CartId":Quote.QuoteId,
                         "QuoteNumber":Quote.CompositeNumber,
                                     "MainItem":item["MainItem"],
                                     "Main_ItemName": dataDict[item["MainItem"]][0],
                                     "LineItem": item["LineItem"],
                                     "Line_ItemName": item["Line_ItemName"],
                                     })
result2 = SqlHelper.Upsert(tableInfo)