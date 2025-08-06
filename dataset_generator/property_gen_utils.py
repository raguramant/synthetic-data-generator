properties_list = [
    {"name": {"type": "string", "minLength": 1, "maxLength": 50, "description": "Full name of the individual"}},
    {"subscriber_name": {"type": "string", "minLength": 1, "maxLength": 50, "description": "Name of the subscriber"}},
    {"patient_name": {"type": "string", "minLength": 1, "maxLength": 50, "description": "Name of the patient"}},
    {"first_name": {"type": "string", "minLength": 1, "maxLength": 50, "description": "First name of the individual"}},
    {"last_name": {"type": "string", "minLength": 1, "maxLength": 50, "description": "Last name of the individual"}},
    {"full_name": {"type": "string", "minLength": 1, "maxLength": 100, "description": "Full name of the individual"}},
    {"organization_name": {"type": "string", "minLength": 1, "maxLength": 50, "description": "Name of the organization"}},
    {"company_name": {"type": "string", "minLength": 1, "maxLength": 50, "description": "Name of the company"}},
    {"organization": {"type": "string", "minLength": 1, "maxLength": 50, "description": "Name of the organization"}},
    {"company": {"type": "string", "minLength": 1, "maxLength": 50, "description": "Name of the company"}},
    {"department": {"type": "string", "minLength": 1, "maxLength": 50, "description": "Department of the individual"}},
    {"age": {"type": "integer", "minimum": 0, "maximum": 120, "description": "Age of the individual"}},
    {"email": {"type": "string", "format": "email", "description": "Email address of the individual"}},
    {"address": {"type": "string", "minLength": 1, "maxLength": 100, "description": "Home address of the individual"}},
    {"phone": {"type": "string", "pattern": "^\\+?[0-9\\- ]{7,15}$", "description": "Phone number of the individual"}},
    {"gender": {"type": "string", "enum": ["male", "female", "other"], "description": "Gender of the individual"}},
    {"date_of_birth": {"type": "string", "format": "date", "description": "Date of birth of the individual"}},
    {"date_of_admission": {"type": "string", "format": "date", "description": "Date of admission to the hospital"}},
    {"date_of_discharge": {"type": "string", "format": "date", "description": "Date of discharge from the hospital"}},
    {"surgery_date": {"type": "string", "format": "date", "description": "Date of surgery"}},
    {"is_covered": {"type": "boolean", "description": "Indicates if the individual is covered by insurance"}},
    {"insurance_id": {"type": "string", "minLength": 1, "maxLength": 50, "description": "Insurance ID of the individual"}},
    {"policy_number": {"type": "string", "minLength": 1, "maxLength": 50, "description": "Policy number of the insurance"}},
    {"policy_start_date": {"type": "string", "format": "date", "description": "Start date of the insurance policy"}},
    {"policy_end_date": {"type": "string", "format": "date", "  description": "End date of the insurance policy"}},
    {"insurance_provider": {"type": "string", "minLength": 1, "maxLength": 50, "description": "Name of the insurance provider"}},
    {"insurance_plan": {"type": "string", "minLength": 1, "maxLength": 50, "description": "Type of insurance plan"}},
    {"medical_record_number": {"type": "string", "minLength": 1, "maxLength": 50, "description": "Medical record number of the individual"}},
    {"social_security_number": {"type": "string", "pattern": "^\\d{3}-\\d{2}-\\d{4}$", "description": "Social Security Number of the individual"}},
    {"npi_number": {"type": "string", "pattern": "^\\d{10}$", "description": "National Provider Identifier number"}},
    {"created_at": {"type": "string", "format": "date-time", "description": "Timestamp when the record was created"}},
    {"updated_at": {"type": "string", "format": "date-time", "description": "Timestamp when the record was last updated"}},
    {"country": {"type": "string", "minLength": 1, "maxLength": 50, "description": "Country of the individual"}},
    {"city": {"type": "string", "minLength": 1, "maxLength": 50, "description": "City of the individual"}},
    {"postal_code": {"type": "string", "minLength": 1, "maxLength": 20, "description": "Postal code of the individual"}},
    {"website": {"type": "string", "format": "uri", "minLength": 1, "maxLength": 100, "description": "Website of the individual"}},
    {"specialization": {"type": "string", "minLength": 1, "maxLength": 50, "description": "Specialization of the healthcare provider"}},
    {"blood_type": {"type": "string", "enum": ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"], "description": "Blood type of the individual"}},
    {"height_cm": {"type": "number", "minimum": 0, "maximum": 180, "description": "Height of the individual in centimeters"}},
    {"weight_kg": {"type": "number", "minimum": 0, "maximum": 200, "description": "Weight of the individual in kilograms"}},
    {"allergies": {"type": "array", "items": {"type": "string"},"maxItems": 10, "description": "Allergies of the individual"}},
    {"medical_conditions": {"type": "array", "items": {"type": "string"}, "description": "Medical conditions of the individual"}},
    {"medications": {"type": "array", "items": {"type": "string"}, "description": "Medications of the individual"}},
    {"emergency_contact": {"type": "object", "description": "Emergency contact information"}},
    {"last_checkup_date": {"type": "string", "format": "date", "description": "Date of last checkup"}},
    {"doctor_name": {"type": "string", "description": "Name of the individual's doctor"}},
    {"smoker": {"type": "boolean", "description": "Indicates if the individual is a smoker"}},
    {"alcohol_consumption": {"type": "string", "enum": ["none", "occasional", "regular"], "description": "Alcohol consumption habits of the individual"}},
    {"heart_rate": {"type": "integer", "minimum": 0, "description": "Heart rate of the individual"}},
    {"blood_pressure": {"type": "string", "pattern": "^(\\d{1,3})/(\\d{1,3})$", "description": "Blood pressure of the individual (systolic/diastolic)"}},
    # Health insurance related fields
    {"service_type": {"type": "string", "minLength": 1, "maxLength": 50, "description": "Type of service provided (e.g., consultation, surgery)"}},
    {"service_type_code": {"type": "string", "minLength": 1, "maxLength": 50, "description": "Code representing the type of service"}},
    {"benefits": {"type": "array", "items": {"type": "string"}, "description": "List of benefits covered by the insurance"}},
    {"claim_number": {"type": "string", "minLength": 1, "maxLength": 50, "description": "Claim number for insurance purposes"}},
    {"claim_charge_amount": {"type": "number", "minimum": 0, "description": "Charge amount for the claim"}},
    {"claim_status": {"type": "object", "properties": {
        "status": {"type": "string", "enum": ["approved", "denied", "pending"], "description": "Status of the claim"},
        "claimstatus_code": {"type": "string", "minLength": 1, "maxLength": 50, "description": "Code representing the claim status"}
    }}}
]

def get_dataset_version(file_name_prefix, dataset_path="../data/"):

    # get the latest version of the dataset
    files = [f for f in os.listdir(dataset_path) if f.startswith(file_name_prefix) and f.endswith('.jsonl')]

    # extract the version numbers from the filenames
    versions = []
    for file in files:
        version_str = file[(len(file_name_prefix)+1):].split('.')[0]  # Extract version part
        try:
            version = int(version_str)
            versions.append(version)
        except ValueError:
            continue  # Skip files that do not match the expected format
    
    #sort the versions in descending order and get the latest one
    versions.sort(reverse=True)
    if versions:
        latest_version = versions[0]
        print(f"Latest version found: {latest_version}")
    else:
        latest_version = 0
        print("No valid dataset versions found. Starting with version 1.")

    next_version =  latest_version + 1  # Increment to get the next version number
    
    return next_version