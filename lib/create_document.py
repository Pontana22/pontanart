from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def create_document(credentials, content: str, options: dict):
    try:
        service = build("docs", "v1", credentials=credentials)
        document = service.documents().create(body={"title":options['docname']}).execute()
        document_id = document.get("documentId")
        end_index = len(content) + 1

        requests = []
            
        # write text
        requests.append({
            "insertText": {
                "text": content,
                "location": {
                    "index": 1
                }
            }
        })
            
        # change line spacing
        requests.append({
            "updateParagraphStyle": {
                "range": {
                    "startIndex": 1,
                    "endIndex": end_index
                },
                "paragraphStyle": {
                    "lineSpacing":options['row_spacing']
                },
                "fields": "lineSpacing"
            }
        })
        
        # change font and text size
        requests.append({
            "updateTextStyle": {
                "range": {
                    "startIndex": 1,
                    "endIndex": end_index
                },
                "textStyle": {
                    "weightedFontFamily": {
                        "fontFamily": options['font_family']
                    },
                    "fontSize": {
                        "magnitude": options['font_size'],
                        "unit": "PT"
                    }
                },
                "fields": "weightedFontFamily, fontSize, foregroundColor"
            }
        })

        service.documents().batchUpdate(documentId=document_id, body={"requests": requests}).execute()

    except HttpError as err:
        exit(err)
