function checkPass(){
    let password = document.getElementById("userInput").value;
    fetch("/password",{
        method: "POST",
        headers:{
            "Content-Type": "application/json"
        },
        body: JSON.stringify({PASS: password})
    })




    .then(response => response.json())
    .then(data =>{
        document.getElementById("result").innerText = "Feedback:    " + data.RESPASS;
    })
}