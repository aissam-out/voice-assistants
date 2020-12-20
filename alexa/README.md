# Alexa

<img src="../images/alexa_logo.png" alt="alexa logo">

Amazon Alexa, also known simply as Alexa, is a virtual assistant AI technology developed by Amazon. It is capable of voice interaction and can also control several smart devices using itself as a home automation system [[1]](https://en.wikipedia.org/wiki/Amazon_Alexa).

## Alexa skills

Amazon allows developers to build and publish skills for Alexa using the Alexa Skills Kit known as Alexa Skills. These third-party-developed skills, once published, are available across Alexa-enabled devices [[2]](https://en.wikipedia.org/wiki/Amazon_Alexa#Alexa_Skills_Kit).

#### 0. Create an account

If you don’t have an [Amazon Developer account](https://developer.amazon.com), create a free one.

#### 1. Create a skill

Go to the [Amazon Developer Console](https://developer.amazon.com/alexa/console/ask) and create an application by clicking on *"Create Skill"* and following the instructions. Select *Custom* to develop an app from scratch.

#### 2. Invocation name

In the *Build* section, select *Invocation* and write a phrase by which a person could trigger this particular skill.

<img src="../images/invocation.PNG" alt="invocation">

#### 3. Intents

Intents are kind of the actions that your Alexa skill performs. In the left hand menu, select *Intent* then *Add* to create a custom intent. Define sample utterances with which users can call up this intent. Preferably [[3]](https://www.ionos.com/digitalguide/online-marketing/online-sales/create-alexa-skills/) add around 30 samples to allow the deep learning algorithm behind Alexa skill to train efficiently and therefore detect this intent in various situations.

<img src="../images/intents.PNG" alt="intents">

As you might have noticed, *{name}* acts as a variable carrying the name we want to send to our back-end. In Amazon's language, those variable are called *slots*. Amazon provides a number of built in slot types, such as dates, numbers, durations, time, etc. But developers can create custom slots for variables which are specific to their skill.


:warning: Do not forget to *save model* and *build model* every time you make changes to the model.

#### 4. Endpoint

Select *Endpoint* in the left hand menu, then add a web service https link to your backend application as in [this example](./alexa_emails/).
