from django.core.management.base import BaseCommand
from advance_crud.models import Student
from django.core.files.base import ContentFile
import random


class Command(BaseCommand):

    help = "Seed database with students"

    def handle(self, *args, **kwargs):

        students = [
           {
        "name": "Rahul Sharma",
        "email": "rahul@gmail.com",
        "age": 20,
        "city": "Delhi",
        "contact_no": "9876543210"
    },
    {
        "name": "Priya Verma",
        "email": "priya@gmail.com",
        "age": 21,
        "city": "Meerut",
        "contact_no": "9876543211"
    },
    {
        "name": "Aman Gupta",
        "email": "aman@gmail.com",
        "age": 22,
        "city": "Noida",
        "contact_no": "9876543212"
    },

    # 30 More Students

    {
        "name": "Neha Singh",
        "email": "neha@gmail.com",
        "age": 19,
        "city": "Lucknow",
        "contact_no": "9876543213"
    },
    {
        "name": "Rohit Kumar",
        "email": "rohit@gmail.com",
        "age": 23,
        "city": "Kanpur",
        "contact_no": "9876543214"
    },
    {
        "name": "Simran Kaur",
        "email": "simran@gmail.com",
        "age": 20,
        "city": "Punjab",
        "contact_no": "9876543215"
    },
    {
        "name": "Arjun Mehta",
        "email": "arjun@gmail.com",
        "age": 24,
        "city": "Mumbai",
        "contact_no": "9876543216"
    },
    {
        "name": "Karan Patel",
        "email": "karan@gmail.com",
        "age": 22,
        "city": "Ahmedabad",
        "contact_no": "9876543217"
    },
    {
        "name": "Sneha Joshi",
        "email": "sneha@gmail.com",
        "age": 21,
        "city": "Pune",
        "contact_no": "9876543218"
    },
    {
        "name": "Vikas Yadav",
        "email": "vikas@gmail.com",
        "age": 23,
        "city": "Agra",
        "contact_no": "9876543219"
    },
    {
        "name": "Pooja Sharma",
        "email": "pooja@gmail.com",
        "age": 20,
        "city": "Jaipur",
        "contact_no": "9876543220"
    },
    {
        "name": "Deepak Chauhan",
        "email": "deepak@gmail.com",
        "age": 22,
        "city": "Dehradun",
        "contact_no": "9876543221"
    },
    {
        "name": "Anjali Mishra",
        "email": "anjali@gmail.com",
        "age": 19,
        "city": "Bhopal",
        "contact_no": "9876543222"
    },
    {
        "name": "Saurabh Jain",
        "email": "saurabh@gmail.com",
        "age": 25,
        "city": "Indore",
        "contact_no": "9876543223"
    },
    {
        "name": "Nisha Gupta",
        "email": "nisha@gmail.com",
        "age": 21,
        "city": "Patna",
        "contact_no": "9876543224"
    },
    {
        "name": "Ravi Verma",
        "email": "ravi@gmail.com",
        "age": 20,
        "city": "Chandigarh",
        "contact_no": "9876543225"
    },
    {
        "name": "Tanya Kapoor",
        "email": "tanya@gmail.com",
        "age": 22,
        "city": "Gurgaon",
        "contact_no": "9876543226"
    },
    {
        "name": "Mohit Saxena",
        "email": "mohit@gmail.com",
        "age": 24,
        "city": "Faridabad",
        "contact_no": "9876543227"
    },
    {
        "name": "Aditi Roy",
        "email": "aditi@gmail.com",
        "age": 20,
        "city": "Kolkata",
        "contact_no": "9876543228"
    },
    {
        "name": "Yash Thakur",
        "email": "yash@gmail.com",
        "age": 23,
        "city": "Shimla",
        "contact_no": "9876543229"
    },
    {
        "name": "Komal Arora",
        "email": "komal@gmail.com",
        "age": 21,
        "city": "Amritsar",
        "contact_no": "9876543230"
    },
    {
        "name": "Harsh Agarwal",
        "email": "harsh@gmail.com",
        "age": 22,
        "city": "Bareilly",
        "contact_no": "9876543231"
    },
    {
        "name": "Payal Singh",
        "email": "payal@gmail.com",
        "age": 20,
        "city": "Aligarh",
        "contact_no": "9876543232"
    },
    {
        "name": "Manish Tiwari",
        "email": "manish@gmail.com",
        "age": 24,
        "city": "Varanasi",
        "contact_no": "9876543233"
    },
    {
        "name": "Ritika Sharma",
        "email": "ritika@gmail.com",
        "age": 19,
        "city": "Mathura",
        "contact_no": "9876543234"
    },
    {
        "name": "Abhishek Pandey",
        "email": "abhishek@gmail.com",
        "age": 23,
        "city": "Ayodhya",
        "contact_no": "9876543235"
    },
    {
        "name": "Shreya Nair",
        "email": "shreya@gmail.com",
        "age": 22,
        "city": "Kerala",
        "contact_no": "9876543236"
    },
    {
        "name": "Raj Malhotra",
        "email": "raj@gmail.com",
        "age": 25,
        "city": "Ludhiana",
        "contact_no": "9876543237"
    },
    {
        "name": "Kriti Sen",
        "email": "kriti@gmail.com",
        "age": 21,
        "city": "Ranchi",
        "contact_no": "9876543238"
    },
    {
        "name": "Adarsh Kumar",
        "email": "adarsh@gmail.com",
        "age": 20,
        "city": "Jammu",
        "contact_no": "9876543239"
    },
    {
        "name": "Megha Bansal",
        "email": "megha@gmail.com",
        "age": 22,
        "city": "Surat",
        "contact_no": "9876543240"
    },
    {
        "name": "Akash Singh",
        "email": "akash@gmail.com",
        "age": 23,
        "city": "Ghaziabad",
        "contact_no": "9876543241"
    },
    {
        "name": "Isha Malhotra",
        "email": "isha@gmail.com",
        "age": 20,
        "city": "Rohtak",
        "contact_no": "9876543242"
    }
]

        for student in students:
            Student.objects.create(
                name=student['name'],
                email=student['email'],
                age=student['age'],
                city=student['city'],
                contact_no=student['contact_no']
            )

        self.stdout.write(
            self.style.SUCCESS("Students Added Successfully")
        )