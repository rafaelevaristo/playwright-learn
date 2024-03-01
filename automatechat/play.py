from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500 )
    contextAna = browser.new_context(
        record_video_dir="videosana/",
    record_video_size={"width": 640, "height": 480}
    )
    pageAna = contextAna.new_page()
    pageAna.goto("https://tlk.io/b6ee98")
    pageAna.get_by_placeholder("Name").click()
    pageAna.get_by_placeholder("Name").fill("alopas")
    pageAna.get_by_placeholder("Name").press("Enter")
    pageAna.get_by_placeholder("alopas...").click()
    pageAna.get_by_placeholder("alopas...").fill("bom dia! Aqui fala a ana")


    contextPaulo = browser.new_context(
        record_video_dir="videospaulo/",
    record_video_size={"width": 640, "height": 480}
    )
    pagePaulo = contextPaulo.new_page()
    pagePaulo.goto("https://tlk.io/b6ee98")
    pagePaulo.get_by_placeholder("Name").click()
    pagePaulo.get_by_placeholder("Name").fill("Paulo")
    pagePaulo.get_by_placeholder("Name").press("Enter")
    pagePaulo.get_by_placeholder("Paulo...").click()
    pagePaulo.get_by_placeholder("Paulo...").fill("bom dia! Aqui fala o Paulo!!!")



    pageAna.wait_for_timeout(5000)


    pageAna.pause()

    # ---------------------
    contextAna.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
