# langchain-agent-streamlit
LLM Agent using LangChain and Streamlit

![wallpaper.jpg](wallpaper.jpg)

## 1 Installation

#### 1.1 Install dependencies

```bash
virtualenv -p python3 .env 
source .env/bin/activate
pip install -r requirements.txt
```

#### 1.2 Set environment variables

```bash
export OPENAI_API_KEY="#####"
```

## 2 Testing

#### 2.1 Ask a question to the agent

```bash
python3 ask.py "What are the latest regulations affecting data privacy in the California?"
```
```bash
The latest regulations affecting data privacy in California are primarily governed by the California Consumer Privacy Act (CCPA) and the California Privacy Rights Act (CPRA). 

The CCPA, which went into effect on January 1, 2020, gives California residents more control over their personal information held by businesses. It requires businesses to disclose data collection and sharing practices, provide opt-out options, and allow consumers to request deletion of their data.

The CPRA, which was approved by California voters in November 2020 and will be fully enforced starting in 2023, expands on the CCPA by introducing new data privacy rights and obligations for businesses. It establishes a new data protection agency, enhances consumer rights, and imposes stricter requirements on businesses handling personal information.

Both the CCPA and CPRA aim to enhance data privacy protections for California residents and impose obligations on businesses to ensure the security and confidentiality of personal information. It is important for startups in California to comply with these regulations to avoid potential fines and legal consequences.
```

#### 2.2 Keep asking. The agent remembers

```bash
python3 ask.py "Tell me more about the second regulation that you mentioned."
```
```bash
The second regulation I mentioned is the California Consumer Privacy Act (CCPA). This regulation gives California residents the right to know what personal information is being collected about them, the right to access that information, and the right to request that their information be deleted. It also requires businesses to disclose their data collection and sharing practices and to obtain explicit consent before collecting personal information. The CCPA applies to businesses that meet certain criteria, such as having annual gross revenues over $25 million or collecting personal information from 50,000 or more consumers. Compliance with the CCPA is important for startups operating in California to protect consumer data and avoid potential fines for non-compliance.
```

#### 2.3 Ask the agent to search the web for news

```bash
python3 ask.py "Can you search the web to see if the are new regulations?"
```
```bash
Invoking: `duckduckgo_search` with `{'query': 'new regulations for startups in California'}`

On October 8, 2023, California Governor Gavin Newsom signed into law Senate Bill 54 ("SB 54"), which will apply to a majority of U.S.venture capital investment firms, even if they are not based in California.
SB 54 aims to tackle the ongoing issue of underrepresentation of certain ethnicities, races, genders, and disability statuses in the venture capital industry by requiring specific diversity measures to be implemented.
This guide provides a roadmap to tackle the key legal steps involved in getting a startup off the ground successfully in California.
The first step is to choose a business structure, with common options including LLC, S-Corp, C-Corp, Partnership, and Sole Proprietorship, each having different legal and taxIt seems that on October 8, 2023, California Governor Gavin Newsom signed Senate Bill 54 ("SB 54"), which aims to address the underrepresentation of certain groups in the venture capital industry.
This bill will impact U.S. venture capital investment firms, even those not based in California.
Additionally, there are key legal steps outlined for startups in California, starting with choosing a suitable business structure such as LLC, S-Corp, C-Corp, Partnership, or Sole Proprietorship.
It's essential to consider the legal and tax implications of each option.
```
