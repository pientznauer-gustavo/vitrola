from winrt.windows.media.control import GlobalSystemMediaTransportControlsSessionManager
import asyncio

async def get_media():
    manager = await GlobalSystemMediaTransportControlsSessionManager.request_async()
    tocando = manager.get_current_session()
    app = tocando.source_app_user_model_id
    media = await tocando.try_get_media_properties_async()
    print(app)
    print(media.album_artist)
    print(media.album_title)
    print(media.title)
asyncio.run(get_media())