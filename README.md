# healthcare-appointments

A Django web application Healthcare care communication platform 

## The Database

![ERD Schema](./ERD.png "ERD Schema")

The application keeps track of three types of users:

 - Patients
 - Providers
 - Admins

Each of these user types are represented as models in the database and each have various levels of privileges.  

## Endpoints

#### MedicationAPI

 - GET
    - returns all medications in the database
    - accessable to `Admin`
 - POST
    - add medications to the database
    - accessable to `Admin`
 - PATCH
    - update medications in the database
    - accessable to `Admin`

#### PrescriptionAPI

 - GET
    - returns prescriptions in the database
    - accessable to `Admin`, `Provider`, `Patient`
 - POST
    - add prescriptions to the database
    - accessable to `Admin`, `Provider`
 - PATCH
    - update prescriptions in the database
    - accessable to `Admin`

#### AdminAPI

 - GET
    - returns all admins in the database
    - accessable to `Admin`

#### AppointmentAPI

 - GET
    - returns appointments in the database
    - accessable to `Admin`, `Provider`, `Patient`
 - POST
    - add appointments to the database
    - accessable to `Admin`, `Provider`, `Patient`
 - PATCH
    - update appointments in the database
    - accessable to `Admin`

#### UserCreationAPI

- POST
    - add patient to the database
    - accessable to `Admin`, `Provider`, `Patient`