# Installation Guide

This guide walks you through setting up DocX on your local machine for development and testing. Ensure your system meets the following prerequisites

## Prerequisites

Before you begin, ensure your system meets these requirements:

- Have the latest versions of npm and Node.js installed.
- Compatible with Windows, Linux, or macOS.

## Installation Steps

### 1. Clone the Repository

Open your terminal and clone the DocX repository using this command

```bash
git clone https://github.com/username/projectname.git
```

### 2. Move into the Project Directory

``` bash
cd projectname
```

### 3. Install Dependencies

Use npm to install necessary project dependencies

```bash
npm install
```

### 4. Set Up the .env File

Create a `.env` file in your root folder and add the following keys

```bash
# Database Configuration
DATABASE_URL=
NEXT_PUBLIC_SUPABASE_URL=
NEXT_PUBLIC_SUPABASE_ANON_KEY=
SERVICE_ROLE_KEY=
PW=
NEXT_PUBLIC_SITE_URL=

# Stripe Configuration
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=
STRIPE_SECRET_KEY=
STRIPE_WEBHOOK_SECRET=
```

### 5. Configuring the Database

1. **Register for a Supabase Account**

    Sign up for a Supabase account at [Supabase](https://supabase.com) if you don't have one yet.

2. **Create a Project**

    - Log in and create a new project, providing project details such as the project name and the closest region (e.g., "south-asia").
    - Before creating the project, ensure you paste the project password into the `.env` file under the `PW` section.

3. **Retrieve Keys from Supabase**

    After project creation, gather the required security keys:

    - **Anonymous Key**: Access your project page in Supabase and locate the anon key. Paste it into the `.env` file at `NEXT_PUBLIC_SUPABASE_ANON_KEY`.
    - **Service Role Key**: In your Supabase project settings, reveal the service role key. Copy and paste it into the `.env` file at `SERVICE_ROLE_KEY`.

4. **Database URL and Host**

    Copy the URL and host information from your Supabase project:

    - **Database URL**: Paste the URL into the `.env` file at `DATABASE_URL`.
    - **Host**: Copy the host information and paste it into the `.env` file at `NEXT_PUBLIC_SUPABASE_URL`.

5. **Set Site URL**

    Ensure that the `NEXT_PUBLIC_SITE_URL` in the `.env` file is configured to `http://localhost:3000/`. This local URL is crucial for the project to operate correctly.

    ```bash
    NEXT_PUBLIC_SITE_URL=http://localhost:3000/
    ```

**NOTE**: In case of missed page of security keys in supabase. Go to the "Settings" tab and navigate to the "Database" section. You'll find all the necessary security keys there.

### 6. Start the Web Server

Run the following command in the terminal:

```bash
npm run dev
```

Once the server starts, access DocX via the provided link in your web browser.

### 7. Email Templates

- In Supabase project dashboard, navigate to Authentication > Email templates.
- Paste the content of [Email template](./emailTemplate.html) into the email template area.
- Save the template.

### 8. Buckets

- In the Supabase dashboard, go to the Storage tab.
- Create three buckets manually: "avatars," "workspace-logos," and "file-banners."

### 9. Policy Setup for Storage Buckets

1. **Accessing Policies**

    Go to the Supabase project dashboard & navigate to the "Storage" tab. Then, Click on "Policies" in the sidebar.

2. **Creating Policies**

    - For each bucket ("avatars," "workspace-logos," and "file-banners"):
    - Select one bucket at a time.
    - Click on "New Policy" and choose "Full Customization."

3. **Policy Configuration**

    - Name the policy as "Allow all access."
    - Check all the checkboxes for allowed operations (Select, Insert, Update, Delete).
    - Under "Target Role," select "Authenticated."
    - Save the policy for each bucket.

    **Note:** This setup ensures that authenticated users have full access to perform operations (select, insert, update, delete) on the specified buckets.

### 10. SQL Editor

- In the Supabase dashboard, go to the SQL editor tab.
- Click on "Stripe Subscription" in the sidebar.
- Paste the content of [Stripe Subscription SQL](./StripeSubscription.sql) into the editor area and run it.

### 11. Stripe Payment Setup

1. **Account Creation on Stripe**

    - Create an account on Stripe by providing all necessary details.
    - In the Stripe dashboard, locate the API section to find the Stripe publishable key and secret key.
    - Copy these keys and update your `.env` file with `NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY` & `STRIPE_SECRET_KEY` respectively.

2. **Setting Up Webhooks**

    In the Stripe dashboard, proceed to set up webhooks. (Continue to step 12 after this section)

    - Click on "Webhooks". Then, click on "Test in a local environment".
    - Copy the first command or provided command:

        ```bash
        stripe login
        ```

    - Paste and run this command in your terminal.
    - One new terminal and then Paste the second & most important command with some modifications.

        ```bash
        stripe listen --forward-to localhost:3000/api/webhook
        ```

      This command should run whenever the project starts.
    - Next, paste and run the third or following command in the terminal

        ```bash
        stripe trigger payment_intent.succeeded
        ```

### 12. Stripe CLI Installation (Windows)

For Windows users, follow these steps to install the Stripe CLI:

- Visit [scoop.sh](https://scoop.sh/) and follow the instructions to install the Scoop package manager. which has around two commands to be run on terminal
- After installing Scoop, proceed with the Stripe CLI installation from the [Stripe CLI GitHub repository](https://github.com/stripe/stripe-cli?tab=readme-ov-file) by selecting the Windows option.
- Copy the provided commands and paste them into your terminal to install the Stripe CLI.

### 13. Product Creation

- In the Stripe dashboard, navigate to the "Product" section under the product catalog.
- Create product names and pricing for your offerings.

Follow these steps carefully. If you encounter any issues during installation, refer to the error messages or reach out to our support team for assistance. Enjoy using Taskflow for development and testing purposes!
