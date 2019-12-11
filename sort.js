function returnLink() {
    let arrayString = document.getElementById("textArray");
    let array = arrayString.value.trim().split(",");
    let duplicateArray = [];
    for (let i = 0; i < array.length; i++) {
        duplicateArray.push(parseInt(array[i]));
    }
    let resArray = "  ";
    for (let i = 0; i < duplicateArray.length; i++) {
        resArray += duplicateArray[i] + "    ";
    }
    document.write(
        `<html>
            <head>
                <style rel="stylesheet" type="text/css">
                    .body{
                        margin: 0;
                        padding: 0;
                    }
                    #styleIt{
                        margin: 10px;
                        padding: 10px;
                        background-color: cornsilk;
                        color: darkmagenta;
                    }
                </style>
            </head>
            <body>
                <div id="styleIt">
                    <p>
                        <center> 
                            Array before sorting: [${resArray}]
                        </center>
                    </p>
                </div>    
            </body>
        </html>`
    )
    for (let i = 0; i < duplicateArray.length-1; i++) {
        for (let j = i+1; j < duplicateArray.length; j++) {
            if (duplicateArray[i] > duplicateArray[j]) {
                let temp = duplicateArray[i];
                duplicateArray[i] = duplicateArray[j];
                duplicateArray[j] = temp;
            }
            document.write(
                `<html>
                    <head>
                        <style rel="stylesheet" type="text/css">
                            .body{
                                margin: 0;
                                padding: 0;
                            }
                            #styleIt{
                                margin: 10px;
                                padding: 10px;
                                background-color: cornsilk;
                                color: darkmagenta;
                            }
                        </style>
                    </head>
                    <body>
                        <div id="styleIt">
                            <p>
                                <center>
                                    ${duplicateArray[i]} and ${duplicateArray[j]} elements had swapped their places.
                                </center>
                            </p>
                        </div>    
                    </body>
                </html>`
            )
            let resArray1 = "";
            for (let i = 0; i < duplicateArray.length; i++) {
                resArray1 += duplicateArray[i] + "    ";
            }
            document.write(
                `<html>
                    <head>
                        <style rel="stylesheet" type="text/css">
                            .body{
                                margin: 0;
                                padding: 0;
                            }
                            #styleIt{
                                margin: 10px;
                                padding: 10px;
                                background-color: cornsilk;
                                color: darkmagenta;
                            }
                        </style>
                    </head>
                    <body>
                        <div id="styleIt">
                            <p>
                                <center>
                                    After swapping ${duplicateArray[i]} and ${duplicateArray[j]} elements the array looks like as follows:<br> 
                                    ${resArray1}
                                </center>
                            </p>
                        </div>    
                    </body>
                </html>`
            )
        }
    }
    resArray = "  ";
    for (let i = 0; i < duplicateArray.length; i++) {
        resArray += duplicateArray[i] + "    ";
    }
    document.write(
        `<html>
            <head>
                <style rel="stylesheet" type="text/css">
                    .body{
                        margin: 0;
                        padding: 0;
                    }
                    #styleIt{
                        margin: 10px;
                        padding: 10px;
                        background-color: cornsilk;
                        color: darkmagenta;
                    }
                </style>
            </head>
            <body>
                <div id="styleIt">
                    <p>
                        <center> 
                            Sorted Array: [${resArray}]
                        </center>
                    </p>
                </div>    
            </body>
        </html>`
    )
    // document.write("<html><body><a href=\"https://www.geeksforgeeks.org/bubble-sort/\">bubble-sort</a></body></html>");
}
