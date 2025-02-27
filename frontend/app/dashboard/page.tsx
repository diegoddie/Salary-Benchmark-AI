import { SidebarTrigger } from "@/components/ui/sidebar";
import { SidebarInset } from "@/components/ui/sidebar";
import { AppSidebar } from "@/components/app-sidebar";
import { SidebarProvider } from "@/components/ui/sidebar";
import { Separator } from "@/components/ui/separator";
import { currentUser } from "@clerk/nextjs/server";
import { RequestSalaryCard } from "@/components/Dashboard/RequestSalaryCard";

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
            <div className="flex flex-1 flex-col gap-4 p-4">
              <RequestSalaryCard />
            </div>
          </SidebarInset>
        </SidebarProvider>
      )
}
