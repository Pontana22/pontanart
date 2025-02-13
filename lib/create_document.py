from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def create_document(credentials, document_name: str, content: str, font_family: str, font_size: int, row_spacing: int):
    try:
        service = build("docs", "v1", credentials=credentials)
        document = service.documents().create(body={"title":document_name}).execute()
        _id = document.get("documentId")
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
                    "lineSpacing":row_spacing
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
                        "fontFamily": font_family
                    },
                    "fontSize": {
                        "magnitude": font_size,
                        "unit": "PT"
                    }
                },
                "fields": "weightedFontFamily, fontSize, foregroundColor"
            }
        })

        service.documents().batchUpdate(documentId=_id, body={"requests": requests}).execute()

    except HttpError as err:
        exit(err)
