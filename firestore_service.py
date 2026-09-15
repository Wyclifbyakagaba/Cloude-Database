"""
Firebase Firestore service functions for the FUMU Sports
Cloud Athlete Manager.

This module contains database operations so that the main
application does not need to contain Firebase-specific code.
"""

import os

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


COLLECTION_NAME = "athletes"


def initialize_firestore(key_path="serviceAccountKey.json"):
    """
    Initialize Firebase and return a Firestore client.

    The service account JSON file is used to authenticate
    the Python application with Firebase.
    """

    if not os.path.exists(key_path):
        raise FileNotFoundError(
            f"Firebase credential file was not found: {key_path}"
        )

    if not firebase_admin._apps:
        credential = credentials.Certificate(key_path)
        firebase_admin.initialize_app(credential)

    return firestore.client()


def add_athlete(
    db,
    name,
    age,
    gender,
    sport,
    club,
    phone,
    email,
):
    """
    Add a new athlete document to Firestore.

    Returns the generated Firestore document ID.
    """

    athlete_data = {
        "name": name,
        "age": age,
        "gender": gender,
        "sport": sport,
        "club": club,
        "phone": phone,
        "email": email,
    }

    document_reference = db.collection(COLLECTION_NAME).add(
        athlete_data
    )

    return document_reference[1].id


def get_all_athletes(db):
    """
    Retrieve all athlete documents from Firestore.

    Returns a list of dictionaries containing the document ID
    and athlete information.
    """

    documents = (
        db.collection(COLLECTION_NAME)
        .order_by("name")
        .stream()
    )

    athletes = []

    for document in documents:
        athlete = document.to_dict()
        athlete["id"] = document.id
        athletes.append(athlete)

    return athletes


def get_athlete(db, athlete_id):
    """
    Retrieve one athlete using the Firestore document ID.

    Returns None if the document does not exist.
    """

    reference = db.collection(COLLECTION_NAME).document(athlete_id)
    document = reference.get()

    if not document.exists:
        return None

    athlete = document.to_dict()
    athlete["id"] = document.id

    return athlete


def search_athletes(db, search_text):
    """
    Search athletes by name, sport, club, phone, or email.

    Firestore does not perform a general contains search easily,
    so records are retrieved and filtered in Python.
    """

    search_text = search_text.strip().lower()

    if not search_text:
        return get_all_athletes(db)

    documents = db.collection(COLLECTION_NAME).stream()

    results = []

    for document in documents:
        athlete = document.to_dict()

        searchable_values = [
            athlete.get("name", ""),
            athlete.get("sport", ""),
            athlete.get("club", ""),
            athlete.get("phone", ""),
            athlete.get("email", ""),
        ]

        searchable_text = " ".join(
            str(value) for value in searchable_values
        ).lower()

        if search_text in searchable_text:
            athlete["id"] = document.id
            results.append(athlete)

    results.sort(
        key=lambda item: item.get("name", "").lower()
    )

    return results


def update_athlete(
    db,
    athlete_id,
    name=None,
    age=None,
    gender=None,
    sport=None,
    club=None,
    phone=None,
    email=None
):
    """
    Update an existing athlete.

    Only values that are not None are changed.
    """

    updates = {}

    if name is not None:
        updates["name"] = name

    if age is not None:
        updates["age"] = age

    if gender is not None:
        updates["gender"] = gender

    if sport is not None:
        updates["sport"] = sport

    if club is not None:
        updates["club"] = club

    if phone is not None:
        updates["phone"] = phone

    if email is not None:
        updates["email"] = email

    if not updates:
        return False

    reference = db.collection(COLLECTION_NAME).document(athlete_id)
    reference.update(updates)

    return True


def delete_athlete(db, athlete_id):
    """
    Delete an athlete document from Firestore.
    """

    reference = db.collection(COLLECTION_NAME).document(athlete_id)

    document = reference.get()

    if not document.exists:
        return False

    reference.delete()

    return True