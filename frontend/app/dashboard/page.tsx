import { SidebarTrigger } from "@/components/ui/sidebar";
import { SidebarInset } from "@/components/ui/sidebar";
import { AppSidebar } from "@/components/app-sidebar";
import { SidebarProvider } from "@/components/ui/sidebar";
import { Separator } from "@/components/ui/separator";
import { currentUser } from "@clerk/nextjs/server";

export default async function Page() {
    const user = await currentUser();
    const userEmail = user?.emailAddresses[0]?.emailAddress;
    return (
        <SidebarProvider>   
          <AppSidebar />
          <SidebarInset>
            <header className="bg-white dark:bg-[#09090b] dark:text-white text-black flex h-16 shrink-0 items-center justify-between border-b border-b-black/30 dark:border-b-slate-500 px-3">
                <div className="flex items-center gap-2">
                <SidebarTrigger />
              <Separator orientation="vertical" className="mr-2 h-6" />
                <h1 className="text-2xl md:text-3xl font-semibold">
                {userEmail}
                </h1>
                </div>

            </header>
            <div className="flex flex-1 flex-col gap-4 p-4 bg-blue-700">
              <div className="grid auto-rows-min gap-4 md:grid-cols-3">
                <div className="aspect-video rounded-xl bg-red/500" />
                <div className="aspect-video rounded-xl bg-muted/50" />
                <div className="aspect-video rounded-xl bg-green-500" />
              </div>
              <div className="min-h-[100vh] flex-1 rounded-xl bg-pink-400 md:min-h-min" />
            </div>
          </SidebarInset>
        </SidebarProvider>
      )
}
