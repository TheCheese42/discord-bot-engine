# Discord Bot Engine

Library for making Discord Bot Development and Testing faster.

## Getting Started

Create a Discord Bot Application at <https://discord.com/developers/applications>.

Save the Token somewhere, if you loose it, you will need to generate a new one.

## Understanding the design

### Components

A DBE Application is made of Components. A Component is an independent piece of software that may share data with other Components.
Examples of Components are not just Discord Bots, but also databases or any other arbitrary executable software.

Components are ran as different threads or, optionally, sub-processes, allowing to make use of multiple CPU Cores.

### Secrets

Components often require certain secrets to operate. For example, Discord Bot Tokens or Database credentials.
Secrets are stored in a `.env` ("dotenv") file.

### Configuration

Components may require further configuration aside from Secrets. Every Component may be assigned one Configuration File.
This file is not meant to be edited at runtime but rather to provide options on launch. Runtime configuration should be
managed using a database (including plain files) inside the Component.
