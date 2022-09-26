api is the main App.
docs is the folder where the medi files like resume will be uploaded
urls ahead of /api/:
    "List": "/applicant-list/",
    "Detail View": "/applicant-detail/<str:pk>/",
    "Create": "/applicant-create/",
    "Update": "/applicant-update/<str:pk>/",
    "Delete": "/applicant-delete/<str:pk>/"
