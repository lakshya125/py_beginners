//To read the ODS(Open Office) file in python
import uno
from com.sun.star.beans import PropertyValue

def Main():
  ctx = uno.getComponentContext() 
  smgr = ctx.ServiceManager 
  oDesktop = smgr.createInstanceWithContext( 'com.sun.star.frame.Desktop',ctx)
  oDoc = oDesktop.getCurrentComponent()
  Sheets = oDoc.getSheets()
  oSheet = oDoc.Sheets.getByName('Sheet1')
  NameCell = oSheet.getCellRangeByName("A1") #A complete URL
  FileName = NameCell.String
 
  PropVal = PropertyValue()
  PropVal.Name = 'Hidden'
  PropVal.Value = True
  oDataDoc = oDesktop.loadComponentFromURL(FileName, '_blank', 0, (PropVal,))
  DataSheets = oDataDoc.getSheets()
  DataSheet = DataSheets.getByName("Sheet1")
  DataCell = DataSheet.getCellRangeByName("B1")
 
  TargetCell = oSheet.getCellRangeByName("A10")
  TargetCell.Value = DataCell.Value
  oDataDoc.close(True)
