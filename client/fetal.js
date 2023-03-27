
function onClickedPredictFetalalHealth() {
    console.log("Predict health button clicked");
    var ASTV = document.getElementById("uiAstv").value;
    var ALTV = document.getElementById("uiAltv").value;
    var AC = document.getElementById("uiAcce").value;
    var Median = document.getElementById("uiMedian").value;
    var Mean = document.getElementById("uiMean").value;
    var MSTV = document.getElementById("uiMstv").value;
    var DP = document.getElementById("uiDp").value;
    var Mode = document.getElementById("uiMode").value;
    var Max = document.getElementById("uiMax").value;
    var LB = document.getElementById("uiDl").value;
    var MLTV = document.getElementById("uiMltv").value;
    var UC = document.getElementById("uiUc").value;
    var Est_Fstate = document.getElementById("uiEstimatedFState");
  
    console.log(ASTV)
    console.log(ALTV)
    console.log(AC)
    console.log(Median)
    console.log(Mean)
    console.log(MSTV)
    console.log(DP)
    console.log(Mode)
    console.log(Max)
    console.log(LB)
    console.log(MLTV)
    console.log(UC)
  
    var url = "http://127.0.0.1:5000/predict_fetal_health"; 
  
    $.post(url, {
        ASTV: parseFloat(ASTV),
        ALTV: parseFloat(ALTV),
        AC: parseFloat(AC),
        Median: parseFloat(Median),
        Mean: parseFloat(Mean),
        MSTV: parseFloat(MSTV),
        DP: parseFloat(DP),
        Mode: parseFloat(Mode),
        Max: parseFloat(Max),
        LB: parseFloat(LB),
        MLTV: parseFloat(MLTV),
        UC: parseFloat(UC),
    },function(data, status) {
        console.log("INSIDE FUNC");
        console.log(data.estimated_fetal_state);
        Est_Fstate.innerHTML = "<h2>" + data.estimated_fetal_state.toString() + "</h2>";
        console.log(status);
    });
  }
  
  