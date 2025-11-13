import pandas as pd
df = pd.read_excel("../data/raw/GSAF5.xls")
df.head()
df['Injury'] = df['Injury'].fillna('Unknown').astype(str).str.lower().str.strip()


def classify_injury(text):
    text = str(text).lower().strip()

    if any(word in text for word in ['no injury', 'uninjured','unharmed', 'none']):
        return 'No Injury'

    if any(word in text for word in ['survived', 'recovered', 'escaped', 'rescued', 'lived']):
        return 'Severe Wounds'

    if any(word in text for word in [
        'body not recovered', 'fatal', 'died', 'death', 'deceased',
        'human remains', 'presumed dead'
    ]):
        return 'Fatal Wounds'
    
    if any(word in text for word in [
        'minor', 'scratch', 'abrasion', 'bruise', 'small', 'superficial', 'cut'
    ]):
        return 'Minor Wounds'

    if any(word in text for word in [
        'amputation', 'severe', 'major', 'deep', 'critical', 'massive',
        'laceration', 'bite', 'injured', 'tissue loss'
    ]):
        return 'Severe Wounds'

    return 'Unknown'

df['Injury_Class'] = df['Injury'].apply(classify_injury)

def clean_fatal_column(df):
    df['Fatal Y/N'] = (
        df['Fatal Y/N']
        .astype(str)
        .str.strip()
        .str.upper()
        .replace({
            'UNKNOWN': 'N',
            'F': 'N',
            'M': 'N',
            'NAN': 'N',
            'NQ': 'N',
            '2017': 'N',
            'Y X 2': 'Y',
        })
    )
    return df