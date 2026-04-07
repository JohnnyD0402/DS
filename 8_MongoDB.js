// ============================================================
//  Practical No. 8 – MongoDB
// ============================================================


// ============================================================
//  SECTION 1 : INSTALLATION OF MONGODB COMMUNITY VERSION
// ============================================================

// Step 1: Download MongoDB Community Server from the official MongoDB website.
//         https://www.mongodb.com/try/download/community

// Step 2: Run the installer and select the 'Complete' setup option.

// Step 3: Install MongoDB as a service so it starts automatically with Windows.

// Step 4: Verify MongoDB installation from Command Prompt.
//         Run the following command in CMD:

//         mongod --version


// ============================================================
//  SECTION 2 : CREATING DATA FOLDER FOR MONGODB
// ============================================================

// MongoDB requires a directory to store database files.
// By default it expects the path  C:\data\db
//
// Step 1: Open File Explorer.
// Step 2: Navigate to Local Disk (C:).
// Step 3: Create a folder named  'data'.
// Step 4: Inside the data folder create another folder named 'db'.
//
// Final folder structure:  C:\data\db
//
// You can also create the folder via CMD with:
//         md C:\data\db


// ============================================================
//  QUESTION 1 – STAFF COLLECTION OPERATIONS
// ============================================================
//  Objective: Create a database Institution and a collection
//  Staff. Insert documents and perform various queries.
// ============================================================

// Step 1: Create / switch to database
use Institution

// Step 2: Insert documents into Staff collection
db.Staff.insertMany([
    { empid: 1,  empname: "Amit",  salary: 45000,  designation: "Clerk"       },
    { empid: 2,  empname: "Ravi",  salary: 60000,  designation: "Manager"     },
    { empid: 3,  empname: "Neha",  salary: 42000,  designation: "Accountant"  },
    { empid: 4,  empname: "Pooja", salary: 80000,  designation: "Manager"     },
    { empid: 5,  empname: "Raj",   salary: 30000,  designation: "Clerk"       },
    { empid: 6,  empname: "Karan", salary: 52000,  designation: "Supervisor"  },
    { empid: 7,  empname: "Sneha", salary: 40000,  designation: "Accountant"  },
    { empid: 8,  empname: "Arjun", salary: 90000,  designation: "Manager"     },
    { empid: 9,  empname: "Meena", salary: 35000,  designation: "Clerk"       },
    { empid: 10, empname: "Vikas", salary: 120000, designation: "Director"    }
])

// Step 3: Display all documents
db.Staff.find()

// Step 4: Display only empid and designation (Projection)
db.Staff.find({}, { empid: 1, designation: 1, _id: 0 })

// Step 5: Sort documents by salary in descending order
db.Staff.find().sort({ salary: -1 })

// Step 6: Display employees with designation Manager OR salary > 50000
db.Staff.find({
    $or: [
        { designation: "Manager"      },
        { salary: { $gt: 50000 }      }
    ]
})

// Step 7: Update salary of all Accountants to 45000
db.Staff.updateMany(
    { designation: "Accountant" },
    { $set: { salary: 45000 } }
)

// Step 8: Remove employees with salary greater than 100000
db.Staff.deleteMany({ salary: { $gt: 100000 } })


// ============================================================
//  QUESTION 2 – STUDENT COLLECTION OPERATIONS
// ============================================================
//  Objective: Create Student collection and perform queries
//  on student data.
// ============================================================

// Insert documents into Student collection
db.Student.insertMany([
    { RollNo: 1,  Name: "Amit",  Class: "BSc", TotalMarks: 350 },
    { RollNo: 2,  Name: "Riya",  Class: "MSc", TotalMarks: 420 },
    { RollNo: 3,  Name: "Rahul", Class: "BSc", TotalMarks: 190 },
    { RollNo: 4,  Name: "Sneha", Class: "MSc", TotalMarks: 450 },
    { RollNo: 5,  Name: "Karan", Class: "BSc", TotalMarks: 380 },
    { RollNo: 6,  Name: "Pooja", Class: "MSc", TotalMarks: 410 },
    { RollNo: 7,  Name: "Arjun", Class: "BSc", TotalMarks: 210 },
    { RollNo: 8,  Name: "Neha",  Class: "MSc", TotalMarks: 470 },
    { RollNo: 9,  Name: "Raj",   Class: "BSc", TotalMarks: 180 },
    { RollNo: 10, Name: "Meena", Class: "MSc", TotalMarks: 430 }
])

// Display all documents
db.Student.find()

// Sort students by TotalMarks in descending order
db.Student.find().sort({ TotalMarks: -1 })

// Display students of class MSc OR TotalMarks greater than 400
db.Student.find({
    $or: [
        { Class: "MSc"                   },
        { TotalMarks: { $gt: 400 }       }
    ]
})

// Remove students with TotalMarks less than 200
db.Student.deleteMany({ TotalMarks: { $lt: 200 } })


// ============================================================
//  QUESTION 3 – MAP REDUCE EXAMPLE
// ============================================================
//  Objective: Calculate total sales by product using MapReduce.
// ============================================================

// Insert documents into sales collection
db.sales.insertMany([
    { "_id": 1, "product": "apple",   "amount": 100 },
    { "_id": 2, "product": "banana",  "amount": 150 },
    { "_id": 3, "product": "apple",   "amount": 200 },
    { "_id": 4, "product": "oranges", "amount": 100 },
    { "_id": 5, "product": "banana",  "amount": 350 },
    { "_id": 6, "product": "oranges", "amount": 200 }
])

// Define Map function
// emit() sends key-value pairs to the reduce function
var mapFunction = function() {
    emit(this.product, this.amount);
};

// Define Reduce function
// Array.sum() aggregates the values for each key
var reduceFunction = function(key, values) {
    return Array.sum(values);
};

// Execute MapReduce and store result in 'total_sales' collection
db.sales.mapReduce(
    mapFunction,
    reduceFunction,
    { out: "total_sales" }
)

// View MapReduce result
db.total_sales.find()
