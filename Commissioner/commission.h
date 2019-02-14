#ifndef COMMISSION_H
#define COMMISSION_H

#include <QString>
#include <QList>
#include <QDate>
#include <float.h>

struct Addition
{
    QString addition;
    float cost;
};


class Commission
{

private:
    QString firstName;
    QString lastName;
    float priceOfPurchase;

    QDate datePlaced;
    QDate dateToShip;
    QDate dateOfCompletion;


    QList<QString> contactInfo;
    QList<QString> supplies;
    QList<QString> features;

    QList<Addition> additions;

public:
    Commission(QString firstName, QString lastName, QString contactInfo);
    Commission(QString firstName, QString lastName, QString contactInfo, float price);

    void addFeature(QString featureToAdd);
    void addContactInfo(QString contactInfo);
    void addAddition(Addition additionToAdd);
    void addSupplies(QString supplyToAdd);

    void setPrice(float priceToSet);
    void setFirstName(QString firstName);
    void setLastName(QString lastName);

    void setDatePlaced(QDate date);
    void setDateToShip(QDate date);
    void setDateOfCompletion(QDate date);

    QString getFirstName();
    QString getLastName();
    float getPrice();
    QDate getDatePlaced();
    QDate getDateToShip();
    QDate getDateOfCompletion();

    QList<QString> getFeatures();
    QList<QString> getSupplies();
    QList<QString> getContactInfo();

    QList<Addition> getAdditions();

};

#endif // COMMISSION_H
