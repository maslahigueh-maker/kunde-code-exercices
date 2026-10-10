
from pathlib import Path
from Part_2_APIS_AI.tavily_search import search_link
from db.supabase_client import supabase
from week3.Part_3_Prompt.prompt_test import get_answer
links = ["https://www.clsottawa.ca/", "https://cscvanier.com/", "https://www.legalaid.on.ca/", "https://ociso.org/"]
#put all your links here

#1
#^ This is for previewing the results only, we want to PRINT the result of the CRAWLING FUNCTION seach_link
def preview_link_results(___):
    for ____ in ____:
        __________
        _________



#2
# ^ we want to do the same thing, but this time,  we want to add all the info form each of the links in a big list so we can extract everything from these websites.
resources_content = []
def crawl_resources(links):
    for link in links:
        result = search_link(link)
        try:
            for i in result["results"]:
                # ^Why are we doing a loop, what are we looping
                if i["raw_content"]:
                    _______._______(
                        f"url: {i['url']}\ncontent: {i['raw_content']}"
                    )
        except IndexError:
            print(result["failed_results"][0]["error"])
        except TypeError:
            print(f"Could not retrieve resource for: {link}")
    
    return resources_content




# DON'T TOUCH THIS!


CLEANUP_PROMPT = """
Clean and organize the following website content so it can be used later to extract accurate information about the organization.

Your job is ONLY to clean and organize the content. Do NOT summarize, interpret, infer, or add information.

SOURCE ATTRIBUTION IS CRITICAL:

* Preserve the exact source URL for every piece of information whenever possible.
* Every section or group of facts must clearly identify the source URL they came from.
* Do not combine information from different URLs without showing the relevant source URLs.
* If the same information appears on multiple URLs, you may remove the duplicate, but keep at least one source URL.
* If information differs between pages, keep both pieces of information and show the source URL for each.
* Never assign information to a source URL if it did not come from that page.
* If information comes from another organization or external resource mentioned on the page, clearly identify the external organization/resource and preserve the URL where that information appeared.
* Source attribution should make it possible for a later extraction step to trace every important fact back to the original webpage.

Rules:

* Remove navigation menus, headers, footers, cookie notices, privacy notices, terms of service, social media links, newsletter signups, tracking text, repeated buttons, and other website boilerplate.
* Remove duplicated content that appears multiple times across pages.
* Remove irrelevant content such as unrelated blog posts, news articles, job postings, donation requests, and promotional material when it does not provide useful information about the organization or what it offers.
* Keep factual information about the organization, its programs, services, resources, and activities.
* Keep information about who the organization serves, including age, location, residency, income, status, demographics, or other eligibility requirements.
* Keep application, registration, referral, intake, appointment, and enrollment procedures.
* Keep costs, fees, funding, subsidies, coverage, and whether something is free or paid.
* Keep contact information, including phone numbers, email addresses, addresses, websites, contact forms, and other ways to reach the organization.
* Keep hours of operation and service-specific hours.
* Keep locations and service areas.
* Keep languages offered and interpretation options.
* Keep accessibility information and accommodations.
* Keep requirements, documentation, identification, deadlines, waitlists, restrictions, and other conditions.
* Keep information about how to access or use each specific program, service, or resource.
* Keep important limitations or exceptions.
* Keep information that may help someone determine whether a resource is relevant to them.
* Keep qualifiers such as "for this program", "by referral", "for residents of Ottawa", "available online", "appointment required", or "subject to availability."
* If information applies only to a specific program, service, location, staff member, or resource, keep that distinction clear. Do not turn it into an organization-wide claim.
* If the website mentions another organization or an external resource, keep the relevant information but clearly indicate that it belongs to the external organization or resource.
* Do not combine information from different organizations.
* Do not combine information from different programs or services if their details differ.
* Do not guess, fill gaps, or add information that is not present in the source content.
* Do not change the meaning of the original information.
* Do not remove information simply because it seems unusual or unimportant. If it could help someone understand, access, or evaluate the organization's resources, keep it.

Organize the cleaned content into logical sections based on what is actually present. You may use sections such as ABOUT, PROGRAMS, SERVICES, ELIGIBILITY, COST, CONTACT, LOCATION, HOURS, LANGUAGES, ACCESSIBILITY, HOW TO ACCESS, REQUIREMENTS, and OTHER RELEVANT INFORMATION, but do not create empty sections or force information into an inappropriate category.

For every section, clearly include the relevant source URL(s).

Use this structure:

SECTION NAME

SOURCE: [exact URL]

* Cleaned factual information
* Cleaned factual information

SOURCE: [exact URL]

* Cleaned factual information

If several facts come from the same URL, group them together under that URL rather than repeating the URL for every sentence.

The goal is to reduce website noise while preserving as much potentially useful factual information as possible for a later extraction step. The cleaned output should be easy for another AI to read and should allow every important fact to be traced back to its original webpage.

Return only the cleaned and organized content.
--
Treat the cleaned content as source evidence, not as verified organization-level facts. Before assigning a fact to an organization, check its scope and source. Do not turn general informational statements into organization-specific facts. Do not turn therapist-specific, program-specific, service-specific, or external-organization information into organization-wide information. If a cost, eligibility requirement, language, availability, or other detail is only associated with a specific program, therapist, provider, or external organization, preserve that association. If the source does not explicitly support a field, return "Not found - verify" rather than making an inference.

Do not treat general examples, typical industry prices, tax information, insurance explanations, or statements about private practice as the organization's actual pricing or coverage. Only report an organization's specific cost or coverage when the source explicitly attributes it to that organization or service.
"""

if __name__ == "__main__":
    preview_link_results(links)
    results = crawl_resources(links)
    # ^ what does .join do to a list?
    resource_list = "\n".join(links)
    combined_resources = "\n\n---\n\n".join(results)
    final_prompt = f"""
    {CLEANUP_PROMPT}

    The resources are these websites:
    {resource_list}

    Here is the scraped content:

    {combined_resources}
    """
    final_answer = get_answer(final_prompt)

    output_path = Path(__file__).parent / "cleaned_data.txt"
    output_path.write_text(final_answer, encoding="utf-8")

    print(f"Saved output to: {output_path}")