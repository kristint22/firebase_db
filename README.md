# Overview

My program has a page for inserting data into the cloud database (data_inserting.py), a page for querying and updating data in the database (data_query.py), and a page to delete a single field and then it deletes two documents that in turn deletes a collection (data_deleting.py). 

I decided to write this software because I've always been curious in cloud databases, especially since I already know MySQL and SQL. I understand how those work and how to make it work, but I didn't know the differences are between NoSQL and why companies are going towards cloud databases. So here we are! I decided to create a small database about scientists to give a feel about how to create and manipulate the data!

{Provide a link to your YouTube demonstration. It should be a 4-5 minute demo of the software running, a walkthrough of the code, and a view of the cloud database.}

[Database Demo Video](http://youtube.link.goes.here)

# Cloud Database

The Google Firebase Cloud database is a non-relational database that supports many different programming languages (C++, Java, JavaScript, Python, Swift, Objective-c, etc). This database uses a hierarchical based data structure to orginize your data. The structure is composed of collections and documents. A collection holds several documents, and within the document is a fields that you create to hold the data. You can also create subcollections within the documents to create more of seperation of data and break it down into smaller chunks for the documents to hold. This seperation and layering helps to create that hierarchical structure and makes it easier to query the data and more organized as well.  

My database is about famous scientists. The main collection is scientists, and then it separates into documents for each person. Each documents contains the person's first name, last name, middle name, birth year, death year, and their gender. This creates a very small hierarchal structure that the cloud database is great for.
# Development Environment

### Tools used: 
- Google Firebase
- Vs Studios

### languages & libraries
python3
firebase-admin (pip install --upgrade firebase-admin)

# Useful Websites

- [Google Firebase Quickstart - Python](https://firebase.google.com/docs/firestore/quickstart?authuser=0#python_1)
- [Google Firebase adding/updating data](https://firebase.google.com/docs/firestore/manage-data/add-data?authuser=0)
- [Google Firebase simple and compund queries](https://firebase.google.com/docs/firestore/query-data/queries?authuser=0#collection-group-query)
- [Google Firebase Order and limit data](https://firebase.google.com/docs/firestore/query-data/order-limit-data?authuser=0)
- [Google Firebase print data](https://firebase.google.com/docs/firestore/query-data/get-data?authuser=0)
- [Google Firebase delete data and collections](https://firebase.google.com/docs/firestore/manage-data/delete-data?authuser=0#collections)
- [Github-Google Cloud platform python examples](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/4939eec8552f45f4a259e7dc33080cb12241b296/firestore/cloud-client/snippets.py#L111-L167)


# Future Work

- Create subcollections that the different disciplines of science and then within those seperate based on gender and then create another subcollection to have the scientists of that gender of that science discipline 
- Create screenshots of common queries 
- Receive notifications of when there are changes that happened in the cloud database
- Restructure to have subcollections and have it be more of a hierarchal data structure

# Sources 
Data based on:
- [Ten Historic Female Scientists You Should Know](https://www.smithsonianmag.com/science-nature/ten-historic-female-scientists-you-should-know-84028788/)
- [Famous Male Scientists](https://www.ranker.com/list/famous-male-scientists/reference)