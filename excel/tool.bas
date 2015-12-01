Option Explicit
Option Base 1

Public Rootdatafile As String, Value As String
Public Template As Worksheet, TmplRange As Range
Public UpldSheet As Worksheet, LoadRange As Range
Public raw_last As Integer, col_last As Integer
Public wkBook As Object, ws As Object

Public SaveName As String   '生成文件保存的文件名
Public PlmOutputName As String
Public PlmBomAddFile As String
Public PlmImGroupName As String
Sub SaveAs()

    Application.DisplayAlerts = False
    With ActiveWorkbook
        .SaveAs (SaveName)
        .Close (False)
    End With
    Application.DisplayAlerts = True

End Sub
Sub Data_Copy()

Dim Point As Long

Set TmplRange = Template.Cells(1, 1).CurrentRegion
Set UpldSheet = wkBook.Worksheets("upload")
Set LoadRange = UpldSheet.Cells(1, 1).CurrentRegion

Point = LoadRange.Rows.Count
If Point = 1 Then
TmplRange.Copy Destination:=UpldSheet.Cells(Point, 1)
Else
TmplRange.Copy Destination:=UpldSheet.Cells(Point + 1, 1)
End If

End Sub
Sub Template_sap()

Dim shtcount As Integer
Dim currow As Integer, curcol As Integer

On Error GoTo Endline
'将当前活动工作簿直接赋值
Set wkBook = ActiveWorkbook
Set Template = wkBook.Worksheets("template")

shtcount = 0
If Worksheets.Count < 3 Then
    Exit Sub
End If

For Each ws In wkBook.Worksheets
    If UCase(ws.Name) = "TEMPLATE" Then
        shtcount = shtcount + 1
    End If
    If UCase(ws.Name) = "RAWDATA" Then
        shtcount = shtcount + 1
    End If
     If UCase(ws.Name) = "UPLOAD" Then
        shtcount = shtcount + 1
    End If
Next ws
'验证表格完整性
If shtcount < 3 Then
Endline:
    MsgBox "The data file must contain : " & Chr(13) & _
           " one batch input template sheet with name 'TEMPLATE'" & Chr(13) & _
           " and one sheet with name 'RAWDATA' and one with name 'upload'"
    Exit Sub
End If

With ActiveSheet
raw_last = .Cells(.Rows.Count, "A").End(xlUp).Row
col_last = .Cells(1, .Columns.Count).End(xlToLeft).Column
End With

currow = 3
curcol = 2

With wkBook.Worksheets("rawdata")
Do While (currow <= raw_last)
    For curcol = 1 To col_last
    If Not IsEmpty(.Cells(2, curcol)) Then
        Value = .Cells(currow, curcol).Value
        Template.Cells(.Cells(2, curcol).Value, 5).Value = Value
    End If
    Next curcol
    Application.StatusBar = "processing line: " & currow - 2
    Call Data_Copy
    currow = currow + 1
Loop

wkBook.Worksheets("upload").Activate
ActiveSheet.Cells(1, 1).CurrentRegion.Select

End With

'将当前文档路径+txt文件赋值
Rootdatafile = ActiveWorkbook.Path + "\bdc_recording.txt"
'如果txt文件存在,删除之,防止弹出覆盖对话框
If Dir(Rootdatafile) <> "" Then
    '显示输出txt文件路径
    'MsgBox Rootdatafile
    Kill (Rootdatafile)
Else: MsgBox "文件不存在"
End If

ActiveWorkbook.SaveAs filename:=(Rootdatafile), FileFormat:=xlText
ActiveWorkbook.Close SaveChanges:=False

End Sub
Sub Template_plm()

Dim firstrng As Range

SaveName = ActiveWorkbook.Path + PlmOutputName

With ActiveSheet
raw_last = .Cells(.Rows.Count, "A").End(xlUp).Row
col_last = .Cells(6, .Columns.Count).End(xlToLeft).Column

If .Cells(1).Value = "ImportSheetType=PART" Then
    Set firstrng = .Cells.Find("End Item", LookIn:=xlValues, lookat:=xlWhole, MatchCase:=False).Offset(1, 0)
ElseIf .Cells(1).Value = "ImportSheetType=BOM" Then
    Set firstrng = .Cells.Find("Action", LookIn:=xlValues, lookat:=xlWhole, MatchCase:=False).Offset(1, 0)
Else
    MsgBox "Type类型不符"
    Exit Sub
End If

End With

If raw_last > firstrng.Row Then
    Range(firstrng, Cells(raw_last, col_last)).FillDown
End If

Application.DisplayAlerts = False
With ActiveWorkbook
    .SaveAs (SaveName)
    .Close (False)
End With
Application.DisplayAlerts = True

End Sub
Sub E_26()
'Auto transform E part and 26 part to BOM
Dim rn, i As Integer
Dim arr As Variant

    rn = Range("A65535").End(xlUp).Row
    arr = Array(0, 1)
    [A1].Select
    For i = 1 To rn
        ActiveCell.Offset(1, 0).Rows("1:1").EntireRow.Insert Shift:=xlDown
        ActiveCell.Offset(0, 2).Resize(1, 2).Cut ActiveCell.Offset(1, 0)
        ActiveCell.Offset(2, 0).Select
    Next
    Columns("A:A").Insert Shift:=xlToRight
    Range("A1:A2") = Application.WorksheetFunction.Transpose(arr)
    rn = Range("B65535").End(xlUp).Row
    Range("A1:A2").AutoFill Range("A1").Resize(rn, 1), xlFillCopy
    [A1].CurrentRegion.Columns.AutoFit
    arr = [A1].CurrentRegion

    Workbooks.Open (ActiveWorkbook.Path + PlmBomAddFile)
    With ActiveWorkbook.Worksheets(1)
        .Cells(7, 1).Resize(UBound(arr), 3) = arr
    End With

End Sub
Sub ZPP78()

    SaveName = "D:\批量创建工艺路线工序"

    Application.DisplayAlerts = False
    With ActiveWorkbook
    .SaveAs (SaveName)
    .Close (False)
    End With
    Application.DisplayAlerts = True

End Sub
Sub plm_imgroup()
Dim rn As Integer

    SaveName = ActiveWorkbook.Path + PlmImGroupName

    '调整列顺序
    [K:K].Cut
    [A:A].Insert Shift:=xlToRight
    [K:K].Cut
    [C:C].Insert Shift:=xlToRight
    [F:G].Cut
    [D:D].Insert Shift:=xlToRight

    '填充所属组
    With ActiveSheet
        rn = .Cells(.Rows.Count, "B").End(xlUp).Row
        .Range("A2") = Range("A2").Value
        .Range("D2") = "是"
        .Range("E2") = "是"
        .Range("A2", .Cells(rn, "A")).FillDown
        .Range("D2", .Cells(rn, "E")).FillDown
    End With

    '保存
    Call SaveAs

End Sub
Sub main()
Dim PlmImOptionSet As String
Dim PlmImBomExpression As String

'init
PlmOutputName = "\000_import_plm"
PlmImGroupName = "\005_import_Group"
PlmImOptionSet = "\006_import_OptionSet"
PlmImBomExpression = "\007_import_BomExpression"
PlmBomAddFile = "\021_BOM_import-add.xlsx"


Application.ScreenUpdating = False

'PLM模板
If ActiveSheet.Cells(1, 1) Like "*ImportSheetType*" Then
    Call Template_plm
'E-26BOM转换
ElseIf ActiveWorkbook.Name Like "*E-26*" Then
    Call E_26
    Call Template_plm
    ActiveWorkbook.Close SaveChanges:=False
'ZPP78 工艺路线
ElseIf ActiveWorkbook.Name Like "*ZPP78*" Then
    Call ZPP78
'导入选项组
ElseIf ActiveWorkbook.Name Like "*import_Group*" Then
    Call plm_imgroup
'导入选项集
ElseIf ActiveWorkbook.Name Like "*import_OptionSet*" Then
    SaveName = ActiveWorkbook.Path + PlmImOptionSet
    Call SaveAs
'导入表达式
ElseIf ActiveWorkbook.Name Like "*import_BomExpression*" Then
    SaveName = ActiveWorkbook.Path + PlmImBomExpression
    Call SaveAs
Else
    Call Template_sap
End If

Application.ScreenUpdating = True

End Sub
