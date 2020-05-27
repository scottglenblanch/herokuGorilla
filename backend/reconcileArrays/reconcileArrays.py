from pathlib import Path
pathToThisPythonFile = Path(__file__).resolve()
import sys
# sys.path.append(str(Path(pathToThisPythonFile.parents[1], 'python')))

# import googleSheets.myGoogleSheetsLibrary._myGoogleSheetsFunc as _myGoogleSheetsFunc
# import googleSheets.myGoogleSheetsLibrary._myGspreadFunc as _myGspreadFunc

from pprint import pprint as p
import gspread


def reconcileArraysFunction(runningOnDevelopmentServerBoolean):

    # pathToRepos = _myPyFunc.getPathUpFolderTree(pathToThisPythonFile, 'repos')

    if runningOnDevelopmentServerBoolean:
        p('********************Running on development server****************')
        
        # this works 
        # import reconcileArrays.hiPackage.hiModule
        # reconcileArrays.hiPackage.hiModule.hiFunction()

        # this works 
        # from reconcileArrays.hiPackage import hiModule
        # hiModule.hiFunction()
        
        # this works 
        # from .hiPackage import hiModule
        # hiModule.hiFunction()

        # this works 
        from ..hiPackage import hiModule
        hiModule.hiFunction()




        # import ../horseStable.clydesdale as clydesdale
    else:
        p('********************Not running on development server****************')

    # arrayOfPartsToAddToPath = ['privateData', 'python', 'googleCredentials']

    # pathToCredentialsFileServiceAccount = _myPyFunc.addToPath(pathToRepos, arrayOfPartsToAddToPath + ['usingServiceAccount', 'jsonWithAPIKey.json'])

    # gspObj = gspread.service_account(filename=pathToCredentialsFileServiceAccount)
    # gspSpreadsheet = gspObj.open("Reconcile Arrays")
    # gspFirstArraySheet = gspSpreadsheet.worksheet('firstArray')
    # gspSecondArraySheet = gspSpreadsheet.worksheet('secondArray')
    # gspComparisonSheet = gspSpreadsheet.worksheet('comparison')
    # gspEndingFirstArraySheet = gspSpreadsheet.worksheet('endingFirstArray')
    # gspEndingSecondArraySheet = gspSpreadsheet.worksheet('endingSecondArray')

    # firstArray = gspFirstArraySheet.get_all_values()
    # secondArray = gspSecondArraySheet.get_all_values()

    # firstArrayColumnIndexToCompare = 8
    # secondArrayColumnIndexToCompare = 5

    # comparisonArray = [[''] * len(firstArray[0]) + ['Side-By-Side'] + [''] * len(secondArray[0])]

    # # p(firstArray[0:5])
    # # p(secondArray[14])

    # while firstArray:

    #     currentFirstArrayRow = firstArray.pop(0)
    #     # p(currentFirstArrayRow)
    #     rowToAppend = currentFirstArrayRow + ['']

    #     for secondArrayRowCount, currentSecondArrayRow in enumerate(secondArray):

    #         # p(currentSecondArrayRow)

    #         if currentFirstArrayRow[firstArrayColumnIndexToCompare] == currentSecondArrayRow[secondArrayColumnIndexToCompare]:

    #             secondArrayRowToAppend = secondArray.pop(secondArrayRowCount)
    #             rowToAppend = rowToAppend + currentSecondArrayRow

    #     comparisonArray.append(rowToAppend)


    # # p(comparisonArray[0:2])

    # _myGspreadFunc.clearAndResizeSheets([gspComparisonSheet, gspEndingFirstArraySheet, gspEndingSecondArraySheet])
    # _myGspreadFunc.updateCells(gspComparisonSheet, comparisonArray)
    # _myGspreadFunc.updateCells(gspEndingFirstArraySheet, firstArray)
    # _myGspreadFunc.updateCells(gspEndingSecondArraySheet, secondArray)




# reconcileArraysFunction(True)
