# Frontend Application

## Overview
This is the frontend of the AI-Assisted Shopping System being developed as part of a dissertation project. The frontend is implemented as a Single-Page Application (SPA) using Vue.js.

## Technologies
- Vue.js
- Vite
- Pinia
- Material Symbols

## Project Structure
```
src/
├── assets/            Static assets and global styles
├── components/        Larger reusable interface components
├── elements/          Small highly reusable UI elements
├── router/            Vue Router configuration (and state validation)
├── services/          API services and mock data
├── stores/            Pinia state management stores
├── views/             Application views/pages
├── App.vue            Root Vue component
└── main.js            Application entry point
```

# Environment
The frontend application was developed and tested with the following environment:
- nvm v1.2.2
- npm v20.19.0

## Installation
```
npm i
```

## Run Development Server
```
npm run dev
```

The application will normally run at:
http://localhost:5173

## Build Production Version
```
npm run build
```