import json
import time
import uuid
from urllib import request, error

SERVER_URL = "http://127.0.0.1:8188"

# -----------------------------
# 1️⃣ ComfyUI 워크플로우 JSON
# -----------------------------
workflow_with_api_nodes = r'''
{"id":"88bcf757-1298-432f-885a-db5ab88cf224","revision":0,"last_node_id":54,"last_link_id":54,"nodes":[{"id":5,"type":"EmptyLatentImage","pos":[-95.59717559814453,-571.0374755859375],"size":[300,110],"flags":{},"order":0,"mode":0,"inputs":[{"localized_name":"너비","name":"width","type":"INT","widget":{"name":"width"},"link":null},{"localized_name":"높이","name":"height","type":"INT","widget":{"name":"height"},"link":null},{"localized_name":"배치 크기","name":"batch_size","type":"INT","widget":{"name":"batch_size"},"link":null}],"outputs":[{"localized_name":"잠재 데이터","name":"LATENT","type":"LATENT","slot_index":0,"links":[27]}],"properties":{"cnr_id":"comfy-core","ver":"0.3.33","Node name for S&R":"EmptyLatentImage"},"widgets_values":[1024,1024,1],"color":"#323","bgcolor":"#535"},{"id":42,"type":"Note","pos":[-75.59688568115234,-421.0376281738281],"size":[260,210],"flags":{},"order":1,"mode":0,"inputs":[],"outputs":[],"title":"Note - Empty Latent Image","properties":{"text":""},"widgets_values":["This node sets the image's resolution in Width and Height.\n\nNOTE: For SDXL, it is recommended to use trained values listed below:\n - 1024 x 1024\n - 1152 x 896\n - 896  x 1152\n - 1216 x 832\n - 832  x 1216\n - 1344 x 768\n - 768  x 1344\n - 1536 x 640\n - 640  x 1536"],"color":"#323","bgcolor":"#535"},{"id":45,"type":"PrimitiveNode","pos":[295.5135192871094,-570.4500122070312],"size":[210,82],"flags":{},"order":2,"mode":0,"inputs":[],"outputs":[{"name":"INT","type":"INT","widget":{"name":"steps"},"links":[38,41]}],"title":"steps","properties":{"Run widget replace on values":false},"widgets_values":[25,"fixed"],"color":"#432","bgcolor":"#653"},{"id":47,"type":"PrimitiveNode","pos":[296.2197570800781,-439.43743896484375],"size":[210,82],"flags":{},"order":3,"mode":0,"inputs":[],"outputs":[{"name":"INT","type":"INT","widget":{"name":"end_at_step"},"slot_index":0,"links":[43,44]}],"title":"end_at_step","properties":{"Run widget replace on values":false},"widgets_values":[20,"fixed"],"color":"#432","bgcolor":"#653"},{"id":17,"type":"VAEDecode","pos":[1197.0247802734375,599.3170166015625],"size":[200,50],"flags":{},"order":15,"mode":0,"inputs":[{"localized_name":"잠재 데이터","name":"samples","type":"LATENT","link":25},{"localized_name":"vae","name":"vae","type":"VAE","link":34}],"outputs":[{"localized_name":"이미지","name":"IMAGE","type":"IMAGE","slot_index":0,"links":[28]}],"properties":{"cnr_id":"comfy-core","ver":"0.3.33","Node name for S&R":"VAEDecode"},"widgets_values":[],"color":"#332922","bgcolor":"#593930"},{"id":41,"type":"Note","pos":[1195.4132080078125,699.4724731445312],"size":[312.02081298828125,120],"flags":{},"order":4,"mode":0,"inputs":[],"outputs":[],"title":"Note - VAE Decoder","properties":{"text":""},"widgets_values":["This node will take the latent data from the KSampler and, using the VAE, it will decode it into visible data\n\nVAE = Latent --> Visible\n\nThis can then be sent to the Save Image node to be saved as a PNG."],"color":"#332922","bgcolor":"#593930"},{"id":10,"type":"KSamplerAdvanced","pos":[808.7730102539062,-57.895355224609375],"size":[300,546],"flags":{},"order":13,"mode":0,"inputs":[{"localized_name":"모델","name":"model","type":"MODEL","link":10},{"localized_name":"긍정 조건","name":"positive","type":"CONDITIONING","link":53},{"localized_name":"부정 조건","name":"negative","type":"CONDITIONING","link":12},{"localized_name":"잠재 데이터","name":"latent_image","type":"LATENT","link":27},{"localized_name":"노이즈 추가","name":"add_noise","type":"COMBO","widget":{"name":"add_noise"},"link":null},{"localized_name":"노이즈 시드","name":"noise_seed","type":"INT","widget":{"name":"noise_seed"},"link":null},{"localized_name":"스텝 수","name":"steps","type":"INT","widget":{"name":"steps"},"link":41},{"localized_name":"cfg","name":"cfg","type":"FLOAT","widget":{"name":"cfg"},"link":null},{"localized_name":"샘플러 이름","name":"sampler_name","type":"COMBO","widget":{"name":"sampler_name"},"link":null},{"localized_name":"스케줄러","name":"scheduler","type":"COMBO","widget":{"name":"scheduler"},"link":null},{"localized_name":"시작 스텝","name":"start_at_step","type":"INT","widget":{"name":"start_at_step"},"link":null},{"localized_name":"종료 스텝","name":"end_at_step","type":"INT","widget":{"name":"end_at_step"},"link":43},{"localized_name":"잔여 노이즈 반환","name":"return_with_leftover_noise","type":"COMBO","widget":{"name":"return_with_leftover_noise"},"link":null}],"outputs":[{"localized_name":"잠재 데이터","name":"LATENT","type":"LATENT","slot_index":0,"links":[13]}],"title":"KSampler (Advanced) - BASE","properties":{"cnr_id":"comfy-core","ver":"0.3.33","Node name for S&R":"KSamplerAdvanced"},"widgets_values":["enable",571362792211850,"randomize",25,8,"euler","normal",0,20,"enable"]},{"id":11,"type":"KSamplerAdvanced","pos":[819.1201782226562,608.375],"size":[300,546],"flags":{},"order":14,"mode":0,"inputs":[{"localized_name":"모델","name":"model","type":"MODEL","link":14},{"localized_name":"긍정 조건","name":"positive","type":"CONDITIONING","link":52},{"localized_name":"부정 조건","name":"negative","type":"CONDITIONING","link":24},{"localized_name":"잠재 데이터","name":"latent_image","type":"LATENT","link":13},{"localized_name":"노이즈 추가","name":"add_noise","type":"COMBO","widget":{"name":"add_noise"},"link":null},{"localized_name":"노이즈 시드","name":"noise_seed","type":"INT","widget":{"name":"noise_seed"},"link":null},{"localized_name":"스텝 수","name":"steps","type":"INT","widget":{"name":"steps"},"link":38},{"localized_name":"cfg","name":"cfg","type":"FLOAT","widget":{"name":"cfg"},"link":null},{"localized_name":"샘플러 이름","name":"sampler_name","type":"COMBO","widget":{"name":"sampler_name"},"link":null},{"localized_name":"스케줄러","name":"scheduler","type":"COMBO","widget":{"name":"scheduler"},"link":null},{"localized_name":"시작 스텝","name":"start_at_step","type":"INT","widget":{"name":"start_at_step"},"link":44},{"localized_name":"종료 스텝","name":"end_at_step","type":"INT","widget":{"name":"end_at_step"},"link":null},{"localized_name":"잔여 노이즈 반환","name":"return_with_leftover_noise","type":"COMBO","widget":{"name":"return_with_leftover_noise"},"link":null}],"outputs":[{"localized_name":"잠재 데이터","name":"LATENT","type":"LATENT","slot_index":0,"links":[25]}],"title":"KSampler (Advanced) - REFINER","properties":{"cnr_id":"comfy-core","ver":"0.3.33","Node name for S&R":"KSamplerAdvanced"},"widgets_values":["disable",0,"fixed",25,8,"euler","normal",20,10000,"disable"]},{"id":19,"type":"SaveImage","pos":[1558.4725341796875,553.4407958984375],"size":[565.77001953125,596.3800048828125],"flags":{},"order":16,"mode":0,"inputs":[{"localized_name":"이미지","name":"images","type":"IMAGE","link":28},{"localized_name":"파일명 접두사","name":"filename_prefix","type":"STRING","widget":{"name":"filename_prefix"},"link":null}],"outputs":[],"properties":{"cnr_id":"comfy-core","ver":"0.3.33"},"widgets_values":["ComfyUI"]},{"id":4,"type":"CheckpointLoaderSimple","pos":[-90,-50],"size":[350,100],"flags":{},"order":5,"mode":0,"inputs":[{"localized_name":"체크포인트 파일명","name":"ckpt_name","type":"COMBO","widget":{"name":"ckpt_name"},"link":null}],"outputs":[{"localized_name":"모델","name":"MODEL","type":"MODEL","slot_index":0,"links":[10]},{"localized_name":"CLIP","name":"CLIP","type":"CLIP","slot_index":1,"links":[5,54]},{"localized_name":"VAE","name":"VAE","type":"VAE","slot_index":2,"links":[]}],"title":"Load Checkpoint - BASE","properties":{"cnr_id":"comfy-core","ver":"0.3.33","Node name for S&R":"CheckpointLoaderSimple","models":[{"name":"sd_xl_base_1.0.safetensors","url":"https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_base_1.0.safetensors?download=true","directory":"checkpoints"}]},"widgets_values":["sd_xl_refiner_1.0.safetensors"],"color":"#323","bgcolor":"#535"},{"id":50,"type":"PrimitiveNode","pos":[-458.9957580566406,123.28369903564453],"size":[300,160],"flags":{},"order":6,"mode":0,"inputs":[],"outputs":[{"name":"STRING","type":"STRING","widget":{"name":"text"},"slot_index":0,"links":[46,48]}],"title":"Negative Prompt (Text)","properties":{"Run widget replace on values":false},"widgets_values":["text, watermark"],"color":"#322","bgcolor":"#533"},{"id":51,"type":"PrimitiveNode","pos":[-458.9957580566406,-76.71602630615234],"size":[300,160],"flags":{},"order":7,"mode":0,"inputs":[],"outputs":[{"name":"STRING","type":"STRING","widget":{"name":"text"},"slot_index":0,"links":[49,50]}],"title":"Positive Prompt (Text)","properties":{"Run widget replace on values":false},"widgets_values":["벌 , 꽃 , 나무 \n평화로운 분위기\n푸른 산과 들판\n만화가 아닌 실사"],"color":"#232","bgcolor":"#353"},{"id":53,"type":"GoogleTranslateCLIPTextEncodeNode","pos":[294.1255477397609,9.287608429678668],"size":[400,204],"flags":{},"order":10,"mode":0,"inputs":[{"localized_name":"clip","name":"clip","type":"CLIP","link":54},{"localized_name":"from_translate","name":"from_translate","type":"COMBO","widget":{"name":"from_translate"},"link":null},{"localized_name":"to_translate","name":"to_translate","type":"COMBO","widget":{"name":"to_translate"},"link":null},{"localized_name":"manual_translate","name":"manual_translate","type":"BOOLEAN","widget":{"name":"manual_translate"},"link":null},{"localized_name":"text","name":"text","type":"STRING","widget":{"name":"text"},"link":49}],"outputs":[{"localized_name":"조건","name":"CONDITIONING","type":"CONDITIONING","links":[53]},{"localized_name":"문자열","name":"STRING","type":"STRING","links":null}],"properties":{"cnr_id":"comfyui_custom_nodes_alekpet","ver":"f75fa7d544ee68eba0cf14a7ebb559a19fcf2f0d","Node name for S&R":"GoogleTranslateCLIPTextEncodeNode"},"widgets_values":["auto","en",false,"Manual Trasnlate","벌 , 꽃 , 나무 \n평화로운 분위기\n푸른 산과 들판\n만화가 아닌 실사"]},{"id":7,"type":"CLIPTextEncode","pos":[294.81282349690616,286.598650285],"size":[397.553466796875,142.57814025878906],"flags":{},"order":9,"mode":0,"inputs":[{"localized_name":"clip","name":"clip","type":"CLIP","link":5},{"localized_name":"프롬프트 텍스트","name":"text","type":"STRING","widget":{"name":"text"},"link":46}],"outputs":[{"localized_name":"조건","name":"CONDITIONING","type":"CONDITIONING","slot_index":0,"links":[12]}],"properties":{"cnr_id":"comfy-core","ver":"0.3.33","Node name for S&R":"CLIPTextEncode"},"widgets_values":["text, watermark"],"color":"#322","bgcolor":"#533"},{"id":12,"type":"CheckpointLoaderSimple","pos":[-79.48125226968409,654.906073827247],"size":[325.4814453125,99.73925018310547],"flags":{},"order":8,"mode":0,"inputs":[{"localized_name":"체크포인트 파일명","name":"ckpt_name","type":"COMBO","widget":{"name":"ckpt_name"},"link":null}],"outputs":[{"localized_name":"모델","name":"MODEL","type":"MODEL","slot_index":0,"links":[14]},{"localized_name":"CLIP","name":"CLIP","type":"CLIP","slot_index":1,"links":[20,51]},{"localized_name":"VAE","name":"VAE","type":"VAE","slot_index":2,"links":[34]}],"title":"Load Checkpoint - REFINER","properties":{"cnr_id":"comfy-core","ver":"0.3.33","Node name for S&R":"CheckpointLoaderSimple","models":[{"name":"sd_xl_refiner_1.0.safetensors","url":"https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0/resolve/main/sd_xl_refiner_1.0.safetensors?download=true","directory":"checkpoints"}]},"widgets_values":["sd_xl_refiner_1.0.safetensors"],"color":"#323","bgcolor":"#535"},{"id":16,"type":"CLIPTextEncode","pos":[303.02496919763473,1043.1797768794456],"size":[388.5469970703125,121.34178161621094],"flags":{},"order":11,"mode":0,"inputs":[{"localized_name":"clip","name":"clip","type":"CLIP","link":20},{"localized_name":"프롬프트 텍스트","name":"text","type":"STRING","widget":{"name":"text"},"link":48}],"outputs":[{"localized_name":"조건","name":"CONDITIONING","type":"CONDITIONING","slot_index":0,"links":[24]}],"properties":{"cnr_id":"comfy-core","ver":"0.3.33","Node name for S&R":"CLIPTextEncode"},"widgets_values":["text, watermark"],"color":"#322","bgcolor":"#533"},{"id":54,"type":"DeepTranslatorCLIPTextEncodeNode","pos":[296.5206079836197,629.7377669703831],"size":[400,360],"flags":{},"order":12,"mode":0,"inputs":[{"localized_name":"clip","name":"clip","type":"CLIP","link":51},{"localized_name":"from_translate","name":"from_translate","type":"COMBO","widget":{"name":"from_translate"},"link":null},{"localized_name":"to_translate","name":"to_translate","type":"COMBO","widget":{"name":"to_translate"},"link":null},{"localized_name":"add_proxies","name":"add_proxies","type":"BOOLEAN","widget":{"name":"add_proxies"},"link":null},{"localized_name":"proxies","name":"proxies","type":"STRING","widget":{"name":"proxies"},"link":null},{"localized_name":"auth_data","name":"auth_data","type":"STRING","widget":{"name":"auth_data"},"link":null},{"localized_name":"service","name":"service","type":"COMBO","widget":{"name":"service"},"link":null},{"localized_name":"text","name":"text","type":"STRING","widget":{"name":"text"},"link":50}],"outputs":[{"localized_name":"조건","name":"CONDITIONING","type":"CONDITIONING","links":[52]},{"localized_name":"문자열","name":"STRING","type":"STRING","links":null}],"properties":{"cnr_id":"comfyui_custom_nodes_alekpet","ver":"f75fa7d544ee68eba0cf14a7ebb559a19fcf2f0d","Node name for S&R":"DeepTranslatorCLIPTextEncodeNode"},"widgets_values":["auto","english",false,"","","GoogleTranslator","벌 , 꽃 , 나무 \n평화로운 분위기\n푸른 산과 들판\n만화가 아닌 실사","proxy_hide","authorization_hide"]}],"links":[[5,4,1,7,0,"CLIP"],[10,4,0,10,0,"MODEL"],[12,7,0,10,2,"CONDITIONING"],[13,10,0,11,3,"LATENT"],[14,12,0,11,0,"MODEL"],[20,12,1,16,0,"CLIP"],[24,16,0,11,2,"CONDITIONING"],[25,11,0,17,0,"LATENT"],[27,5,0,10,3,"LATENT"],[28,17,0,19,0,"IMAGE"],[34,12,2,17,1,"VAE"],[38,45,0,11,6,"INT"],[41,45,0,10,6,"INT"],[43,47,0,10,11,"INT"],[44,47,0,11,10,"INT"],[46,50,0,7,1,"STRING"],[48,50,0,16,1,"STRING"],[49,51,0,53,4,"STRING"],[50,51,0,54,7,"STRING"],[51,12,1,54,0,"CLIP"],[52,54,0,11,1,"CONDITIONING"],[53,53,0,10,1,"CONDITIONING"],[54,4,1,53,0,"CLIP"]],"groups":[{"id":1,"title":"Base Prompt","bounding":[281.707763671875,-128.8721160888672,439.7534484863281,600.5301513671875],"color":"#3f789e","font_size":24,"flags":{}},{"id":2,"title":"Refiner Prompt","bounding":[285.9026794433594,567.3108520507812,442.127685546875,588.2311401367188],"color":"#3f789e","font_size":24,"flags":{}},{"id":4,"title":"Load in BASE SDXL Model","bounding":[-100,-130,359.4917907714844,403.9964904785156],"color":"#a1309b","font_size":24,"flags":{}},{"id":5,"title":"Load in REFINER SDXL Model","bounding":[-95.2878189086914,564.1364135742188,361.54791259765625,403.3152160644531],"color":"#a1309b","font_size":24,"flags":{}},{"id":6,"title":"Empty Latent Image","bounding":[-115.09705352783203,-652.1575317382812,353.29144287109375,461.8235168457031],"color":"#a1309b","font_size":24,"flags":{}},{"id":7,"title":"VAE Decoder","bounding":[1165.2672119140625,521.2222900390625,358.535400390625,332.57080078125],"color":"#b06634","font_size":24,"flags":{}},{"id":8,"title":"Step Control","bounding":[266.23602294921875,-652.185302734375,274.54791259765625,472.66363525390625],"color":"#3f789e","font_size":24,"flags":{}},{"id":10,"title":"Text Prompts","bounding":[-471.7359313964844,-166.89599609375,339,622],"color":"#3f789e","font_size":24,"flags":{}},{"id":11,"title":"Base","bounding":[-110,-173.60000610351562,1228.77294921875,655.2579956054688],"color":"#3f789e","font_size":24,"flags":{}},{"id":12,"title":"Refiner","bounding":[-105.2878189086914,520.5363159179688,1234.4083251953125,645.005615234375],"color":"#3f789e","font_size":24,"flags":{}}],"config":{},"extra":{"ds":{"scale":0.7613688546265532,"offset":[1266.2252191670243,269.9154486846038]},"frontendVersion":"1.18.9"},"version":0.4}
'''


# -----------------------------
# 2️⃣ 서버에 워크플로우 전송
# -----------------------------
def send_prompt(workflow_json, api_key=None):
    payload = {
        "prompt": workflow_json,
        "extra_data": {},
        "client_id": str(uuid.uuid4()),
    }
    if api_key:
        payload["extra_data"]["api_key_comfy_org"] = api_key

    data = json.dumps(payload).encode("utf-8")
    req = request.Request(
        f"{SERVER_URL}/prompt",
        data=data,
        headers={"Content-Type": "application/json"},
    )

    try:
        with request.urlopen(req) as resp:
            resp_json = json.loads(resp.read().decode("utf-8"))
            prompt_id = resp_json.get("prompt_id")
            print(f"✅ Workflow submitted. prompt_id = {prompt_id}")
            return prompt_id
    except error.HTTPError as e:
        print("❌ HTTP Error:", e.read().decode("utf-8"))
    except Exception as e:
        print("❌ Error sending prompt:", e)
    return None


# -----------------------------
# 3️⃣ /history/{prompt_id} 로 상태 조회
# -----------------------------
def wait_for_result(prompt_id, interval=2):
    history_url = f"{SERVER_URL}/history/{prompt_id}"
    print("⏳ Waiting for ComfyUI to finish...")

    while True:
        try:
            with request.urlopen(history_url) as resp:
                hist_data = json.loads(resp.read().decode("utf-8"))
                outputs = hist_data.get(prompt_id, {}).get("outputs", {})

                # 결과가 존재하면 이미지 목록 출력
                if outputs:
                    print("✅ Generation complete!\n")
                    for node_id, node_data in outputs.items():
                        if "images" in node_data:
                            for img in node_data["images"]:
                                filename = img["filename"]
                                folder = img.get("subfolder", "")
                                print(f"🖼️  Image saved: output/{folder}/{filename}")
                    break
        except error.HTTPError:
            pass
        except Exception:
            pass
        time.sleep(interval)


# -----------------------------
# 3️⃣ 워크플로우 UI 형식을 API 형식으로 변환
# -----------------------------
def convert_workflow_to_api_format(workflow):
    """
    ComfyUI UI 워크플로우 형식을 API 형식으로 변환
    UI 형식: {"nodes": [...], "links": [...]}
    API 형식: {"node_id": {"class_type": "...", "inputs": {...}}}
    """
    api_format = {}

    # UI 전용 노드 타입 (실행에 불필요)
    skip_node_types = ["Note", "MarkdownNote"]

    # PrimitiveNode 값들을 저장
    primitive_values = {}
    for node in workflow.get("nodes", []):
        if node["type"] == "PrimitiveNode" and "widgets_values" in node:
            primitive_values[str(node["id"])] = node["widgets_values"][0]

    # link_id -> (source_node_id, output_index) 매핑 생성
    link_map = {}
    for link in workflow.get("links", []):
        link_id = link[0]
        source_node_id = str(link[1])
        output_index = link[2]
        link_map[link_id] = (source_node_id, output_index)

    # nodes 배열을 순회하며 API 형식으로 변환
    for node in workflow.get("nodes", []):
        node_id = str(node["id"])
        node_type = node["type"]

        # UI 전용 노드는 건너뛰기
        if node_type in skip_node_types or node_type == "PrimitiveNode":
            continue

        # inputs 구성
        inputs = {}

        # widget 값들을 inputs에 추가
        if "widgets_values" in node and node["widgets_values"]:
            # 노드 타입에 따라 위젯 값 매핑
            if node_type == "KSamplerAdvanced":
                widget_names = ["add_noise", "noise_seed", "control_after_generate", "steps", "cfg",
                               "sampler_name", "scheduler", "start_at_step", "end_at_step", "return_with_leftover_noise"]
                for i, value in enumerate(node["widgets_values"]):
                    if i < len(widget_names):
                        inputs[widget_names[i]] = value
            elif node_type == "EmptyLatentImage":
                if len(node["widgets_values"]) >= 3:
                    inputs["width"] = node["widgets_values"][0]
                    inputs["height"] = node["widgets_values"][1]
                    inputs["batch_size"] = node["widgets_values"][2]
            elif node_type == "CheckpointLoaderSimple":
                if node["widgets_values"]:
                    inputs["ckpt_name"] = node["widgets_values"][0]
            elif node_type in ["CLIPTextEncode"]:
                if node["widgets_values"] and len(node["widgets_values"]) > 0:
                    inputs["text"] = node["widgets_values"][0] if isinstance(node["widgets_values"][0], str) else ""
            elif node_type == "GoogleTranslateCLIPTextEncodeNode":
                widget_names = ["from_translate", "to_translate", "manual_translate", "text", "manual_translation"]
                for i, value in enumerate(node["widgets_values"]):
                    if i < len(widget_names):
                        inputs[widget_names[i]] = value
            elif node_type == "DeepTranslatorCLIPTextEncodeNode":
                widget_names = ["from_translate", "to_translate", "add_proxies", "proxies",
                               "auth_data", "service", "text", "proxy_hide", "authorization_hide"]
                for i, value in enumerate(node["widgets_values"]):
                    if i < len(widget_names):
                        inputs[widget_names[i]] = value
            elif node_type == "SaveImage":
                if node["widgets_values"]:
                    inputs["filename_prefix"] = node["widgets_values"][0]

        # 입력 연결 처리
        if "inputs" in node:
            for input_item in node["inputs"]:
                link_id = input_item.get("link")
                input_name = input_item["name"]

                if link_id is not None and link_id in link_map:
                    source_node_id, output_index = link_map[link_id]

                    # PrimitiveNode에서 온 값인 경우 직접 값 사용
                    if source_node_id in primitive_values:
                        inputs[input_name] = primitive_values[source_node_id]
                    else:
                        # 일반 노드 연결
                        inputs[input_name] = [source_node_id, output_index]

        api_format[node_id] = {
            "class_type": node_type,
            "inputs": inputs
        }

    return api_format


# -----------------------------
# 4️⃣ 실행
# -----------------------------
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Send prompt to ComfyUI API")
    parser.add_argument("--text", type=str, default="masterpiece best quality man", help="Text prompt for CLIPTextEncode node")
    parser.add_argument("--seed", type=int, default=None, help="Seed for KSampler node")
    args = parser.parse_args()

    # 워크플로우 로드
    workflow = json.loads(workflow_with_api_nodes)

    # args.text가 제공되면 Positive Prompt PrimitiveNode(ID: 51)의 값을 업데이트
    if args.text:
        for node in workflow.get("nodes", []):
            if node["type"] == "PrimitiveNode" and node["id"] == 51:
                node["widgets_values"][0] = args.text
                break

    # args.seed가 제공되면 KSamplerAdvanced(ID: 10)의 시드 값을 업데이트
    if args.seed is not None:
        for node in workflow.get("nodes", []):
            if node["type"] == "KSamplerAdvanced" and node["id"] == 10:
                node["widgets_values"][1] = args.seed  # noise_seed는 두 번째 위젯
                break

    # API 형식으로 변환
    prompt2 = convert_workflow_to_api_format(workflow)

    prompt_id = send_prompt(prompt2)
    if prompt_id:
        wait_for_result(prompt_id)
