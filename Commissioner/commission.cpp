#include "commission.h"

Commission::Commission(QString firstName, QString lastName, QString contactInfo)
{
    this->firstName = firstName;
    this->lastName = lastName;
    this->contactInfo.append(contactInfo);

}

Commission::Commission(QString firstName, QString lastName, QString contactInfo, float price)
{
    this->firstName = firstName;
    this->lastName = lastName;
    this->contactInfo.append(contactInfo);
    this->priceOfPurchase = price;
}

void Commission::addFeature(QString featureToAdd)
{
    this->features.append(featureToAdd);
}

void Commission::addContactInfo(QString contactInfo)
{
    this->contactInfo.append(contactInfo);
}

void Commission::addAddition(Addition additionToAdd)
{
    this->additions.append(additionToAdd);
}

void Commission::addSupplies(QString supplyToAdd)
{
    this->supplies.append(supplyToAdd);
}

void Commission::setPrice(float priceToSet)
{
    this->priceOfPurchase = priceToSet;
}

void Commission::setFirstName(QString firstName)
{
    this->firstName = firstName;
}

void Commission::setLastName(QString lastName)
{
    this->lastName = lastName;
}

void Commission::setDatePlaced(QDate date)
{
    this->datePlaced = date;
}

void Commission::setDateToShip(QDate date)
{
    this->dateToShip = date;
}

void Commission::setDateOfCompletion(QDate date)
{
    this->dateOfCompletion = date;
}

QString Commission::getFirstName()
{
    return firstName;
}

QString Commission::getLastName()
{
    return lastName;
}

float Commission::getPrice()
{
    return priceOfPurchase;
}

QDate Commission::getDatePlaced()
{
    return datePlaced;
}

QDate Commission::getDateToShip()
{
    return dateToShip;
}

QDate Commission::getDateOfCompletion()
{
    return dateOfCompletion;
}

QList<QString> Commission::getFeatures()
{
    return features;
}

QList<QString> Commission::getSupplies()
{
    return supplies;
}

QList<QString> Commission::getContactInfo()
{
    return contactInfo;
}

QList<Addition> Commission::getAdditions()
{
    return additions;
}
