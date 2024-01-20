function validateForm() {
    var name = document.bookings.fname.value;
    var surname = document.bookings.fsurname.value;
    var email = document.bookings.femail.value;
    if (name == "" || surname == "" || email == "") {
        alert("All the fields are mandatory");
        return false;
    }
    alert("Booking complete")
    return true
}