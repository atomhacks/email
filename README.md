# atomhacks/email

This is what we use to send emails out to everyone in Bronx Science Hackers. It has only been tested on macOS, but in theory this should work in Linux environments as well.

## Setup

### Install Python dependencies

First, make sure you have Python 3.6 and pip installed. Then run the following command to install all necessary dependencies:

```bash
$ pip install -r requirements.txt
```

### Authenticate with AWS

After that command finishes, you'll need to verify that your computer authenticated with AWS. We use `boto3` for AWS requests, so you should refer to the [Boto 3 documentation](https://boto3.readthedocs.io/en/latest/guide/quickstart.html#configuration) to figure out how to get yourself set up. You should also make sure that your credentials are configured to work with [Amazon SES](https://aws.amazon.com/ses/).

### Set up your Google Sheet

We read names and email addresses from a Google Sheet, so you'll need to set one up that we'll be able to use. It should look something like this:

|Email address|First name|Last name|
|:-|:-|:-|
|example@email.com|Jack|Cook|
|example2@email.com|Barack|Obama|
|example3@email.com|John|Smith|

[Here's an example](https://docs.google.com/spreadsheets/d/1luDE6PCo2CCBuQAF51bfig9GACMSBQh1c6oX9aw3n64/edit?usp=sharing) of a spreadsheet that would work correctly.

Once you've created your sheet, copy its ID from the URL (the long alphanumeric string) and paste it into the value for `spreadsheet_id` in the `config.json` file.

### Generate a Google Sheets API key

Go to the [credentials page](https://console.developers.google.com/apis/credentials) in the Google Developers API Console and generate an API key. Make sure that the project that the key belongs to has the Google Sheets API enabled. Once you have your key, paste it into the value for `google_api_key` in the `config.json` file.

After this last step, you should be all set up to send some emails!

## Usage

### Write the email that you want to send

Write out your email, following the format of the `.email` files that already exist. Once you're done writing, place your new file in the `emails` folder. Keep in mind that the line breaks in your file matter, as these determine where your paragraphs will start and end.

While writing your emails, you can use `{{first}}` to indicate that each member's first name should be put there, `{{last}}` to indicate that each member's last name should be put there, and `{{email}}` to indicate that each member's email address should be put there. Using these variables comes with the benefit of making your emails personalized, but however your emails will now take longer to send. This is because each email will now have to be sent individually as opposed to the same email being sent out to everyone.

### Send your email out to everyone

By now, with everything is in place, you should be able to send your email from the command line. Perform the following command where `filename` is the name of the file that you just created.

```bash
$ python send.py example
You are about to send "Welcome to atomhacks/email!" to 3 people.
Do you want to continue? [Y/n]
Email to example@email.com was sent successfully!
Email to example2@email.com was sent successfully!
Email to example3@email.com was sent successfully!
```

## License

`email` is available under the MIT license. See the LICENSE file for details.
