
function onClickedPredictMaternalHealth() {
  console.log("Predict health button clicked");
  var Age = document.getElementById("uiAge").value;
  var SystolicBP = document.getElementById("uiSbp").value;
  var DiastolicBP = document.getElementById("uiDbp").value;
  var BS = document.getElementById("uiBs").value;
  var BodyTemp = document.getElementById("uiBodyTemp").value;
  var HeartRate = document.getElementById("uiHeartRate").value;
  var Est_state = document.getElementById("uiEstimatedState");

  console.log(Age)
  console.log(SystolicBP)
  console.log(DiastolicBP)
  console.log(BS)
  console.log(BodyTemp)
  console.log(HeartRate)

  var url = "http://127.0.0.1:5000/predict_maternal_health"; 

  $.post(url, {
      Age: parseFloat(Age),
      SystolicBP: parseFloat(SystolicBP),
      DiastolicBP: parseFloat(DiastolicBP),
      BS: parseFloat(BS),
      BodyTemp: parseFloat(BodyTemp),
      HeartRate: parseFloat(HeartRate),
  },function(data, status) {
      console.log("INSIDE FUNC");
      console.log(data.estimated_maternal_state);
      Est_state.innerHTML = "<h2>" + data.estimated_maternal_state.toString() + "</h2>";
      console.log(status);
  });
}

