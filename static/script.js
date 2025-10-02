// функция обновления данных датчиков
function updateData() {
    fetch('/sensors')
        .then(response => response.json())
        .then(data => {
            document.getElementById('temp').innerText = data.temperature.toFixed(1);
            document.getElementById('pressure').innerText = data.pressure.toFixed(2);
            document.getElementById('oil_level').innerText = data.oil_level.toFixed(1);
            document.getElementById('oilLevel').style.height = data.oil_level + "%";
            document.getElementById('pump_status').innerText = data.pump_status;
        });
}

setInterval(updateData, 2000);
updateData(); 
