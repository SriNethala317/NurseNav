document.getElementById("nurseLogin").addEventListener("click", e => {
    e.preventDefault();
    document.querySelector("#selection").classList.add("hide");
    document.querySelector("#missionStatement").classList.add("hide");
    document.querySelector("#nurse").classList.remove("hide");
    document.querySelector("#buttons").classList.remove("hide");
});

document.getElementById("userLogin").addEventListener("click", e => {
    e.preventDefault();
    document.querySelector("#selection").classList.add("hide");
    document.querySelector("#missionStatement").classList.add("hide");
    document.querySelector("#user").classList.remove("hide");
    document.querySelector("#buttons").classList.remove("hide");
});

document.getElementById("back").addEventListener("click", e => {
    document.querySelector("#selection").classList.remove("hide");
    document.querySelector("#nurse").classList.add("hide");
    document.querySelector("#user").classList.add("hide");
    document.querySelector("#buttons").classList.add("hide");
    document.querySelector("#missionStatement").classList.remove("hide");
});

