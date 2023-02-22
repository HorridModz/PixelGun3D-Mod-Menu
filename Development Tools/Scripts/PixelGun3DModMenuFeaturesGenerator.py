import sys

_CodePath = r"C:/Users/zachy/AndroidStudioProjects/PixelGun3D-Mod-Menu/app/src/main/jni/Main.cpp"
_FeaturesPath = r"C:/Users/zachy/AndroidStudioProjects/PixelGun3D-Mod-Menu/app/src/main/jni/Hacks/Features.hpp"
_OutputPath = r"C:\Users\zachy\OneDrive\Documents\Work\Temp\Python Temps\modmenucode.cpp"

log = []
def logmessage(message):
    log.append(message)

def loadcode():
    global Code
    with open(_CodePath) as f:
        Code = f.read()
    return(Code)

def getfeaturesstring(code):
    return(code[code.find("    const char *features[] = {") + len("    const char *features[] = {\n"):code.find("\n    };\n\n    //Now you dont have to manually update the number everytime;")])

def parsefeatures(featuresstring):
    rawelements = featuresstring.split("\n")
    incategory = None
    collapsename = None
    parsedfeatures = []
    for element in rawelements:
        if element.lstrip().startswith("//"):
            continue
        strippedelement = element[element.find("OBFUSCATE(\"") + len("OBFUSCATE(\""):element.find("\"),")]
        elementdata = strippedelement.split("_")
        parsedfeature = {}
        if elementdata[0] == "Category":
            incategory = elementdata[1]
        else:
            if elementdata[0] == "Collapse":
                collapsename = elementdata[1]
            else:
                try:
                    int(elementdata[0])
                except ValueError:
                    parsedfeature["FeatNum"] = None
                else:
                    parsedfeature["FeatNum"] = elementdata[0]
                    del elementdata[0]
                if elementdata[0] == "CollapseAdd":
                    parsedfeature["Collapse"] = collapsename
                    del elementdata[0]
                else:
                    parsedfeature["Collapse"] = None
                parsedfeature["Category"] = incategory
                parsedfeature["Type"] = elementdata[0]
                ignore = ["RichTextView","RichWebView","ButtonLink"]
                valid = True
                for item in ignore:
                    if item == parsedfeature["Type"]:
                        valid = False
                        break
                if not(valid):
                    logmessage("Ignoring Feature: " + parsedfeature["Type"])
                    continue
                if parsedfeature["Type"] in ["InputText","InputValue","SeekBar","Toggle","CheckBox"]:
                    if parsedfeature["Type"] in ["Toggle","CheckBox"]:
                        if elementdata[1] == "True":
                            parsedfeature["DefaultTrue"] = True
                            del elementdata[1]
                        else:
                            parsedfeature["DefaultTrue"] = False
                parsedfeature["Name"] = elementdata[1]
                parsedfeatures.append(parsedfeature)
    return(parsedfeatures)

def generatecategories(features):
    #categories: Keys = categories, Items = dicts of collapses
    #Collapses: Keys = collapsename, Items = dicts of features
    categories = {}
    for feature in features:
        #print(feature["Type"])
        category = feature["Category"]
        collapse = feature["Collapse"]
        featnum = feature["FeatNum"]
        try:
            name = feature["Name"]
        except:
            print(feature)
            raise BaseException(log)
        strippedname = feature["Type"] + "_" + feature["Name"].replace("Don't","Disable").replace("don't","disable").title().replace(" ","").replace("\t","").replace("\"","").replace("'","").replace("-","").replace(".","").replace(",","").replace(";","").replace("\\","").replace("/","").replace("$","").replace("#","").replace("!","").replace("@","").replace("%","").replace("^","").replace("*","").replace(")","").replace("(","").replace("[","").replace("]","").replace("`","").replace(":","")
        funcname = name.replace("Don't","Disable").replace("don't","disable").title().replace(" ","").replace("\t","").replace("\"","").replace("'","").replace("-","").replace(".","").replace(",","").replace(";","").replace("\\","").replace("/","").replace("$","").replace("#","").replace("!","").replace("@","").replace("%","").replace("^","").replace("*","").replace(")","").replace("(","").replace("[","").replace("]","").replace("`","").replace(":","")
        if feature["Type"] == "InputText":
            varname = feature["Type"] + "_" + feature["Name"].replace("Don't","Disable").replace("don't","disable").title().replace(" ","").replace("\t","").replace("\"","").replace("'","").replace("-","").replace(".","").replace(",","").replace(";","").replace("\\","").replace("/","").replace("$","").replace("#","").replace("!","").replace("@","").replace("%","").replace("^","").replace("*","").replace(")","").replace("(","").replace("[","").replace("]","").replace("`","").replace(":","")
            funcname = "Set" + feature["Type"] + "_" + feature["Name"].replace("Don't","Disable").replace("don't","disable").title().replace(" ","").replace("\t","").replace("\"","").replace("'","").replace("-","").replace(".","").replace(",","").replace(";","").replace("\\","").replace("/","").replace("$","").replace("#","").replace("!","").replace("@","").replace("%","").replace("^","").replace("*","").replace(")","").replace("(","").replace("[","").replace("]","").replace("`","").replace(":","")
            datatype = "std::string"
            default = "\"{[Default]}\""
            valueparam = True
        elif feature["Type"] == "InputValue":
            varname = feature["Type"] + "_" + feature["Name"].replace("Don't","Disable").replace("don't","disable").title().replace(" ","").replace("\t","").replace("\"","").replace("'","").replace("-","").replace(".","").replace(",","").replace(";","").replace("\\","").replace("/","").replace("$","").replace("#","").replace("!","").replace("@","").replace("%","").replace("^","").replace("*","").replace(")","").replace("(","").replace("[","").replace("]","").replace("`","").replace(":","")
            funcname = "Set" + feature["Type"] + "_" + feature["Name"].replace("Don't","Disable").replace("don't","disable").title().replace(" ","").replace("\t","").replace("\"","").replace("'","").replace("-","").replace(".","").replace(",","").replace(";","").replace("\\","").replace("/","").replace("$","").replace("#","").replace("!","").replace("@","").replace("%","").replace("^","").replace("*","").replace(")","").replace("(","").replace("[","").replace("]","").replace("`","").replace(":","")
            datatype = "int"
            default = "1"
            valueparam = True
        elif feature["Type"] == "SeekBar":
            varname = feature["Type"] + "_" + feature["Name"].replace("Don't","Disable").replace("don't","disable").title().replace(" ","").replace("\t","").replace("\"","").replace("'","").replace("-","").replace(".","").replace(",","").replace(";","").replace("\\","").replace("/","").replace("$","").replace("#","").replace("!","").replace("@","").replace("%","").replace("^","").replace("*","").replace(")","").replace("(","").replace("[","").replace("]","").replace("`","").replace(":","")
            funcname = "Set" + feature["Type"] + "_" + feature["Name"].replace("Don't","Disable").replace("don't","disable").title().replace(" ","").replace("\t","").replace("\"","").replace("'","").replace("-","").replace(".","").replace(",","").replace(";","").replace("\\","").replace("/","").replace("$","").replace("#","").replace("!","").replace("@","").replace("%","").replace("^","").replace("*","").replace(")","").replace("(","").replace("[","").replace("]","").replace("`","").replace(":","")
            datatype = "int"
            default = "1"
            valueparam = True
        elif feature["Type"] in ["Toggle","CheckBox"]:
            #varname = feature["Type"] + "_" + "is" + feature["Name"].replace("Don't","Disable").replace("don't","disable").title().replace(" ","").replace("\t","").replace("\"","").replace("'","").replace("-","").replace(".","").replace(",","").replace(";","").replace("\\","").replace("/","").replace("$","").replace("#","").replace("!","").replace("@","").replace("%","").replace("^","").replace("*","").replace(")","").replace("(","").replace("[","").replace("]","").replace("`","").replace(":","")
            varname = "is" + feature["Name"].replace("Don't","Disable").replace("don't","disable").title().replace(" ","").replace("\t","").replace("\"","").replace("'","").replace("-","").replace(".","").replace(",","").replace(";","").replace("\\","").replace("/","").replace("$","").replace("#","").replace("!","").replace("@","").replace("%","").replace("^","").replace("*","").replace(")","").replace("(","").replace("[","").replace("]","").replace("`","").replace(":","")
            funcname = feature["Type"] + "_" + feature["Name"].replace("Don't","Disable").replace("don't","disable").title().replace(" ","").replace("\t","").replace("\"","").replace("'","").replace("-","").replace(".","").replace(",","").replace(";","").replace("\\","").replace("/","").replace("$","").replace("#","").replace("!","").replace("@","").replace("%","").replace("^","").replace("*","").replace(")","").replace("(","").replace("[","").replace("]","").replace("`","").replace(":","")
            datatype = "bool"
            if feature["DefaultTrue"]:
                default = "true"
            else:
                default = "false"
            valueparam = True
        elif feature["Type"] == "Button":
            varname = feature["Type"] + "_" + "is" + feature["Name"].replace("Don't","Disable").replace("don't","disable").title().replace(" ","").replace("\t","").replace("\"","").replace("'","").replace("-","").replace(".","").replace(",","").replace(";","").replace("\\","").replace("/","").replace("$","").replace("#","").replace("!","").replace("@","").replace("%","").replace("^","").replace("*","").replace(")","").replace("(","").replace("[","").replace("]","").replace("`","").replace(":","")
            funcname = feature["Type"] + "_" + feature["Name"].replace("Don't","Disable").replace("don't","disable").title().replace(" ","").replace("\t","").replace("\"","").replace("'","").replace("-","").replace(".","").replace(",","").replace(";","").replace("\\","").replace("/","").replace("$","").replace("#","").replace("!","").replace("@","").replace("%","").replace("^","").replace("*","").replace(")","").replace("(","").replace("[","").replace("]","").replace("`","").replace(":","")
            datatype = "bool"
            default = "false"
            valueparam = False
        else:
            print(feature)
            raise NotImplementedError("Unsupported Feature Type: " + feature["Type"])
        updatevar = True
        if feature["Type"] in ["Toggle","CheckBox"]:
            firstcallvar = True
        else:
            firstcallvar = False
        if collapse is not None:
            varname = collapse.replace("Don't","Disable").replace("don't","disable").title().replace(" ","").replace("\t","").replace("\"","").replace("'","").replace("-","").replace(".","").replace(",","").replace(";","").replace("\\","").replace("/","").replace("$","").replace("#","").replace("!","").replace("@","").replace("%","").replace("^","").replace("*","").replace(")","").replace("(","").replace("[","").replace("]","").replace("`","").replace(":","") \
                + "_" + varname
            funcname = collapse.replace("Don't","Disable").replace("don't","disable").title().replace(" ","").replace("\t","").replace("\"","").replace("'","").replace("-","").replace(".","").replace(",","").replace(";","").replace("\\","").replace("/","").replace("$","").replace("#","").replace("!","").replace("@","").replace("%","").replace("^","").replace("*","").replace(")","").replace("(","").replace("[","").replace("]","").replace("`","").replace(":","") \
                + "_" + funcname
            strippedname = collapse.replace("Don't","Disable").replace("don't","disable").title().replace(" ","").replace("\t","").replace("\"","").replace("'","").replace("-","").replace(".","").replace(",","").replace(";","").replace("\\","").replace("/","").replace("$","").replace("#","").replace("!","").replace("@","").replace("%","").replace("^","").replace("*","").replace(")","").replace("(","").replace("[","").replace("]","").replace("`","").replace(":","") \
                + "_" + strippedname
        featuredict = {
                "featnum": featnum,
                "name": name,
                "strippedname": strippedname,
                "varname": varname,
                "funcname": funcname,
                "datatype": datatype,
                "default": default,
                "valueparam": valueparam,
                "updatevar": updatevar,
                "firstcallvar": firstcallvar,
                }
        if category in categories:
            if collapse in categories[category]:
                categories[category][collapse].append(featuredict)
            else:
                categories[category][collapse] = [featuredict]
        else:
            categories[category] = {collapse: [featuredict]}
        #print(str(categories).replace("Don't","Disable").replace("don't","disable").replace("'","\"").replace("None","null").replace("True","true").replace("False","false").replace("null:","\"None\":"))
        #print("\n\n\n")
    return(categories)

def generatefeaturesnamespace(categories):
    #Open Features Namespace
    code = "namespace Features {"
    for thiscategoryname in categories.keys():
        thiscategory = categories[thiscategoryname]
        if thiscategoryname is None:
            for (thiscollapsename) in thiscategory.keys():
                thiscollapse = thiscategory[thiscollapsename]
                if thiscollapsename is not None:
                    #Collapse Comment
                    code += "\n\t//Collapse " + thiscollapsename + "\n"
                code += "\n"
                for thisfeature in thiscollapse:
                    #Feature Comment
                    code += "\t//" + thisfeature["name"]
                    code += "\n\t"
                    code += thisfeature["datatype"] + " " + thisfeature["varname"] + " = " + thisfeature["default"] + ";\n\t"
                    #Feature Fields
                    if thisfeature["updatevar"]:
                        code += "bool " + "update" + thisfeature["strippedname"] + " = " + "false" + ";\n\t"
                    if thisfeature["firstcallvar"]:
                        code += "bool " + "is" + thisfeature["strippedname"] + "FirstCall = " + "true" + ";\n\t"
                    # Feature Function
                    code += "void " + thisfeature["funcname"] + "("
                    if thisfeature["valueparam"]:
                        code += thisfeature["datatype"] + " value"
                    code += ") {\n\t\t"
                    if thisfeature["valueparam"]:
                        # InputText / InputValue / Slider / Toggle / Checkbox
                        if thisfeature["firstcallvar"]:
                            code += "if (!" + "is" + thisfeature["strippedname"] + "FirstCall" + ") {\n\t\t\t"
                            code += thisfeature["varname"] + " = value" + ";\n\t\t\t"
                            if thisfeature["updatevar"]:
                                code += "update" + thisfeature["strippedname"] + " = true" + ";\n\t\t"
                            code += "} else {\n\t\t\t"
                            code += "is" + thisfeature["strippedname"] + "FirstCall" + " = false" + ";\n\t\t"
                            code += "}\n\t"
                        else:
                            code += thisfeature["varname"] + " = value" + ";\n\t\t"
                            if thisfeature["updatevar"]:
                                code += "update" + thisfeature["strippedname"] + " = true" + ";\n\t"
                    elif thisfeature["updatevar"]:
                        # Button
                        if thisfeature["firstcallvar"]:
                            code += "if (!" + "is" + thisfeature["strippedname"] + "FirstCall" + ") {\n\t\t\t"
                            code += thisfeature["varname"] + " = true" + ";\n\t\t\t"
                            code += "update" + thisfeature["strippedname"] + " = true" + ";\n\t\t"
                            code += "} else {\n\t\t\t"
                            code += "is" + thisfeature["strippedname"] + "FirstCall" + " = false" + ";\n\t\t"
                            code += "}\n\t"
                        else:
                            code += thisfeature["varname"] + " = true" + ";\n\t"
                    code += "}\n"
        else:
            code += "\n\t"
            #Open Struct
            code += "struct " + thiscategoryname.replace("Don't","Disable").replace("don't","disable").title().replace(" ","").replace("\t","").replace("\"","").replace("'","").replace("-","").replace(".","").replace(",","").replace(";","").replace("\\","").replace("/","").replace("$","").replace("#","").replace("!","").replace("@","").replace("%","").replace("^","").replace("*","").replace(")","").replace("(","").replace("[","").replace("]","").replace("`","").replace(":","") \
                + "Hacks" + " {"
            for (thiscollapsename) in thiscategory.keys():
                thiscollapse = thiscategory[thiscollapsename]
                if thiscollapsename is not None:
                    #Collapse Comment
                    code += "\n\t//Collapse " + thiscollapsename + "\n"
                code += "\n"
                for thisfeature in thiscollapse:
                    # Feature Comment
                    code += "\t//" + thisfeature["name"]
                    code += "\n\t"
                    code += thisfeature["datatype"] + " " + thisfeature["varname"] + " = " + thisfeature[
                        "default"] + ";\n\t"
                    # Feature Fields
                    if thisfeature["updatevar"]:
                        code += "bool " + "update" + thisfeature["strippedname"] + " = " + "false" + ";\n\t"
                    if thisfeature["firstcallvar"]:
                        code += "bool " + "is" + thisfeature["strippedname"] + "FirstCall = " + "true" + ";\n\t"
                    # Feature Function
                    code += "void " + thisfeature["funcname"] + "("
                    if thisfeature["valueparam"]:
                        code += thisfeature["datatype"] + " value"
                    code += ") {\n\t\t"
                    if thisfeature["valueparam"]:
                        # InputText / InputValue / Slider / Toggle / Checkbox
                        if thisfeature["firstcallvar"]:
                            code += "if (!" + "is" + thisfeature["strippedname"] + "FirstCall" + ") {\n\t\t\t"
                            code += thisfeature["varname"] + " = value" + ";\n\t\t\t"
                            if thisfeature["updatevar"]:
                                code += "update" + thisfeature["strippedname"] + " = true" + ";\n\t\t"
                            code += "} else {\n\t\t\t"
                            code += "is" + thisfeature["strippedname"] + "FirstCall" + " = false" + ";\n\t\t"
                            code += "}\n\t"
                        else:
                            code += thisfeature["varname"] + " = value" + ";\n\t\t"
                            if thisfeature["updatevar"]:
                                code += "update" + thisfeature["strippedname"] + " = true" + ";\n\t"
                    elif thisfeature["updatevar"]:
                        # Button
                        if thisfeature["firstcallvar"]:
                            code += "if (!" + "is" + thisfeature["strippedname"] + "FirstCall" + ") {\n\t\t\t"
                            code += thisfeature["varname"] + " = true" + ";\n\t\t\t"
                            code += "update" + thisfeature["strippedname"] + " = true" + ";\n\t\t"
                            code += "} else {\n\t\t\t"
                            code += "is" + thisfeature["strippedname"] + "FirstCall" + " = false" + ";\n\t\t"
                            code += "}\n\t"
                        else:
                            code += thisfeature["varname"] + " = true" + ";\n\t"
                    code += "}\n"
            #Close Struct
            code += "\t};"
            #Create Object From Struct
            code += "\n\t" + thiscategoryname.replace("Don't","Disable").replace("don't","disable").title().replace(" ","").replace("\t","").replace("\"","").replace("'","").replace("-","").replace(".","").replace(",","").replace(";","").replace("\\","").replace("/","").replace("$","").replace("#","").replace("!","").replace("@","").replace("%","").replace("^","").replace("*","").replace(")","").replace("(","").replace("[","").replace("]","").replace("`","").replace(":","") \
                    + "Hacks" + " " + thiscategoryname.replace("Don't","Disable").replace("don't","disable").title().replace(" ","").replace("\t","").replace("\"","").replace("'","").replace("-","").replace(".","").replace(",","").replace(";","").replace("\\","").replace("/","").replace("$","").replace("#","").replace("!","").replace("@","").replace("%","").replace("^","").replace("*","").replace(")","").replace("(","").replace("[","").replace("]","").replace("`","").replace(":","") \
                    + ";"
        code += "\n"
    #Close Features Namespace
    code += "}"
    return(code)

def generatefeaturescases(categories):
    #Open Features Cases
    code = "switch (featNum) {"
    for thiscategoryname in categories.keys():
        thiscategory = categories[thiscategoryname]
        code += "\n\t\t"
        #Category Comment
        if thiscategory is not None:
            code += "//Category " + thiscategoryname + "\n"
        for (thiscollapsename) in thiscategory.keys():
            thiscollapse = thiscategory[thiscollapsename]
            if thiscollapsename is not None:
                #Collapse Comment
                code += "\n\t\t//Collapse " + thiscollapsename
            code += "\n"
            for thisfeature in thiscollapse:
                #Feature Comment
                code += "\n\t\t//" + thisfeature["name"]
                code += "\n\t\t"
                #Feature Case
                code += "case " + thisfeature["featnum"] + ":\n\t\t\t"
                #Feature Function
                if thiscategoryname is None:
                    code += "Features::" + thisfeature["funcname"] + "("
                else:
                    code += "Features::" + thiscategoryname.replace("Don't","Disable").replace("don't","disable").title().replace(" ","").replace("\t","").replace("\"","").replace("'","").replace("-","").replace(".","").replace(",","").replace(";","").replace("\\","").replace("/","").replace("$","").replace("#","").replace("!","").replace("@","").replace("%","").replace("^","").replace("*","").replace(")","").replace("(","").replace("[","").replace("]","").replace("`","").replace(":","") \
                         + "." + thisfeature["funcname"] + "("
                if thisfeature["valueparam"]:
                    if thisfeature["datatype"] == "int":
                        code += "(int)value"
                    elif thisfeature["datatype"] == "std::string":
                        code += "std::string(str != NULL ? env->GetStringUTFChars(str, 0) : " + thisfeature["default"] + ")"
                    elif thisfeature["datatype"] == "bool":
                        code += "(boolean != JNI_FALSE)"
                code += ");\n\t\t\t"
                #Break Case
                code += "break;"
            code += "\n"
    #Close Features Cases
    code += "\n\t}"
    return(code)
            
def addfeatnums(featuresstring,start0 = True,countcollapses = True, countcollapsesseperate = True):                    
    features = featuresstring.split("\n")
    newfeatures = []
    if start0:
        featnum = 0
    else:
        featnum = 1
    collapsefeatnum = 10000
    for feature in features:
        if feature.lstrip().startswith("//"):
            newfeatures.append(feature)
            continue
        strippedfeature = feature[feature.find("OBFUSCATE(\"") + len("OBFUSCATE(\""):feature.find("\"),")]
        ignore = ["Category","RichTextView","RichWebView","ButtonLink"]
        if not(countcollapses and not(countcollapsesseperate)):
            ignore.append("Collapse")
        valid = True
        for item in ignore:
            if (item + "_") in strippedfeature:
                valid = False
                break
        if valid:
            try:
                int(strippedfeature[0:strippedfeature.find("_")])
            except ValueError:
                newfeature = feature.replace("OBFUSCATE(\"","OBFUSCATE(\"" + str(featnum) + "_")
            else:
                newfeature = feature.replace(strippedfeature[0:strippedfeature.find("_")],str(featnum))
            newfeatures.append(newfeature)
            featnum += 1
        else:
            if ("Collapse_") in strippedfeature:
                if countcollapsesseperate:
                    try:
                        int(strippedfeature[0:strippedfeature.find("_")])
                    except ValueError:
                        newfeature = feature.replace("OBFUSCATE(\"","OBFUSCATE(\"" + str(collapsefeatnum) + "_")
                    else:
                        newfeature = feature.replace(strippedfeature[0:strippedfeature.find("_")],str(collapsefeatnum))
                else:
                    try:
                        int(strippedfeature[0:strippedfeature.find("_")])
                    except ValueError:
                        newfeature = feature
                    else:
                        newfeature = feature.replace(strippedfeature[0:strippedfeature.find("_") + 1],"")
                newfeatures.append(newfeature)
                collapsefeatnum += 1
            else:
                newfeatures.append(feature)
    newfeaturesstring = "\n".join(newfeatures)
    return(newfeaturesstring)

loadcode()
with open(_CodePath,"r") as original:
    content = str(original.read())
with open(_OutputPath,"w") as backup:
    backup.write(content)
code = addfeatnums(getfeaturesstring(Code),True,False,False)
with open(_CodePath,"w") as f:
        new = content.replace(content[content.find("    const char *features[] = {") + len("    const char *features[] = {\n"):content.find("\n    };\n\n    //Now you dont have to manually update the number everytime;")],code)
        f.write(new)
loadcode()
parsedfeatures = parsefeatures(getfeaturesstring(Code))
categories = generatecategories(parsefeatures(getfeaturesstring(Code)))
code = generatefeaturesnamespace(categories)
#with open(_OutputPath,"w") as f:
    #f.write(code)
with open(_FeaturesPath,"r") as f:
    featurescontent = f.read()
with open(_FeaturesPath,"w") as f:
        new = featurescontent.replace(featurescontent[featurescontent.find("namespace Features {"):],code)
        f.write(new)
code = generatefeaturescases(categories)
with open(_CodePath,"r") as original:
    content = str(original.read())
#sys.exit(content)
with open(_CodePath,"w") as f:
    if content.find("    }\n    updatehooksready = true;") == -1:
        new = content.replace(content[content.find("switch (featNum) {"):content.find("\t}\n    updatehooksready = true;") + 2],code)
    else:
        new = content.replace(content[content.find("switch (featNum) {"):content.find("    }\n    updatehooksready = true;") + 5],code)
    f.write(new)
#print(str(parsedfeatures).replace("Don't","Disable").replace("don't","disable").replace("'","\"").replace("None","null").replace("True","true").replace("False","false").replace("null:","\"None\":"))
#print(str(categories).replace("Don't","Disable").replace("don't","disable").replace("'","\"").replace("None","null").replace("True","true").replace("False","false").replace("null:","\"None\":"))
